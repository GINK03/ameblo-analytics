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
import optuna
import sys
if '--gender' in sys.argv:
    input_path = 'tmp/C_gender/*.pkl'
    suffix = 'gender'
    max_data_size = 10
elif '--location' in sys.argv:
    input_path = 'tmp/C_location/*.pkl'
    suffix = 'location'
    max_data_size = 30
elif '--location_saitama' in sys.argv:
    input_path = 'tmp/C_location_saitama/*.pkl'
    suffix = 'location_saitama'
    max_data_size = 30
elif '--generation' in sys.argv:
    input_path = 'tmp/C_generation/*.pkl'
    suffix = 'generation'
    max_data_size = 100
else:
    input_path = 'tmp/C/*.pkl'
    suffix = ''
    max_data_size = 10

term_index = json.load(open('tmp/term_index.json'))
index_term = {idx: term for term, idx in term_index.items()}
lils = []
labels = []
for idx, path in enumerate(sorted(Path().glob(input_path))):
    print(idx, path)
    try:
        labels_, lil = pickle.load(path.open('rb'))
    except EOFError as ex:
        continue
    labels.extend(labels_)
    lils.append(lil)
    if idx >= max_data_size:
        break

lils = Vstack(lils).tocsr()
labels = np.array(labels)
# print(dict(Counter(labels.tolist())))


def trainer(l1_ratio, search=True):
    kf = KFold(n_splits=4)
    coefs, aucs = [], []
    for fold, (trn_idx, val_idx) in enumerate(kf.split(lils, labels)):
        model = SGD(loss='log', penalty='elasticnet', max_iter=100000,
                    alpha=0.001, l1_ratio=l1_ratio, n_jobs=-1)
        # - model = LogisticRegression(penalty='elasticnet', solver='saga', l1_ratio=0.15)
        # - model = LinearRegression()
        model.fit(lils[trn_idx], labels[trn_idx])
        pred = model.predict(lils[val_idx])
        aucs.append(roc_auc_score(labels[val_idx], pred))
        coefs.append(model.coef_[0])
        print(roc_auc_score(labels[val_idx], pred))
    coefs = np.array(coefs).mean(axis=0)
    if search is True:
        return np.mean(aucs)*-1
    else:
        term_weight = [(index_term[idx], w) for idx, w in enumerate(coefs)]
        term_weight = sorted(term_weight, key=lambda x: x[1]*-1)
        auc = np.mean(aucs)
        json.dump(term_weight, fp=open(
            f'tmp/term_weight_{auc:0.09f}_{suffix}.json', 'w'), indent=2, ensure_ascii=False)


def objective(trial):
    l1_ratio = trial.suggest_uniform('l1_ratio', 0, 0.5)
    #alpha = trial.suggest_uniform('alpha', 0, 1)
    return trainer(l1_ratio, search=True)


study = optuna.create_study()
study.optimize(objective, n_trials=5)
print(study.best_value)
print(study.best_trial)
best_param = study.best_params
best_param['search'] = False
print('train with best param and dump features.')
print('score', trainer(**best_param))
