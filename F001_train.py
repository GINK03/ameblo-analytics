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
lils = []
labels = []
for idx, path in enumerate(Path().glob('tmp/C/*.pkl')):
    labels_, lil = pickle.load(path.open('rb'))
    labels.extend(labels_)
    lils.append(lil)
    if idx >= 10:
        break

lils = Vstack(lils).tocsr()
labels = np.array(labels)
print(dict(Counter(labels.tolist())))

kf = KFold(n_splits=4)
for fold, (trn_idx, val_idx) in enumerate(kf.split(lils, labels)):
    #model = SGD(loss='log', penalty='elasticnet', alpha=0.0001, l1_ratio=0.15)
    model = LogisticRegression()
    #model = LinearRegression()
    print(trn_idx)
    model.fit(lils[trn_idx], labels[trn_idx])
    pred = model.predict(lils[val_idx])
    print('mae', Mae(labels[val_idx], pred) )
    print('auc', roc_auc_score(labels[val_idx], pred) )

