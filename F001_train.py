import pickle
from pathlib import Path
import numpy as np
from scipy.sparse import vstack as Vstack
from sklearn.linear_model import SGDClassifier as SGD
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
from sklearn.metrics import mean_absolute_error as Mae
from collections import Counter
import json

term_index = json.load(open('tmp/term_index.json'))
index_term = {idx:term for term,idx in term_index.items()}
lils = []
labels = []
for idx, path in enumerate(sorted(Path().glob('tmp/C/*.pkl'))):
    print(idx, path)
    try:
        labels_, lil = pickle.load(path.open('rb'))
    except EOFError as ex:
        continue
    labels.extend(labels_)
    lils.append(lil)
    if idx >= 50:
        break

lils = Vstack(lils).tocsr()
labels = np.array(labels)
# print(dict(Counter(labels.tolist())))

kf = KFold(n_splits=4)
coefs, aucs = [], []
for fold, (trn_idx, val_idx) in enumerate(kf.split(lils, labels)):
    model = SGD(loss='log', penalty='elasticnet', max_iter=50000, alpha=0.1, l1_ratio=0.5, n_jobs=-1)
    # model = LogisticRegression(penalty='elasticnet', solver='saga', l1_ratio=0.15)
    # model = LinearRegression()
    model.fit(lils[trn_idx], labels[trn_idx])
    pred = model.predict(lils[val_idx])
    aucs.append(roc_auc_score(labels[val_idx], pred))
    coefs.append(model.coef_[0])

coefs = np.array(coefs).mean(axis=1)
term_weight = [(index_term[idx], w) for idx, w in enumerate(coefs)]
print(np.mean(aucs))
for term, weight in sorted(term_weight, key=lambda x:x[1]*-1):
    print(term, weight)


