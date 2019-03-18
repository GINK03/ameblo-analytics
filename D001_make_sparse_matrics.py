import pandas as pd
import numpy as np
from pathlib import Path
import json
from scipy.sparse import lil_matrix as Lil
#from scipy.sparse import csr_matrix as Csr
import pickle
from concurrent.futures import ProcessPoolExecutor as PPE
import random
term_index = json.load(open('tmp/term_index.json'))

def pmap(arg):
    ii, path = arg
    print(path)
    df = pd.read_csv(path)
    df = df[['time', 'label', 'body']]
    labels = []
    lil  = Lil((len(df), len(term_index),))
    for idx, (time, label, body) in enumerate(zip(df['time'], df['label'], df['body'])):
        #if label == 0 and random.random() >= 0.2:
        #    continue
        labels.append(label)
        for term in str(body).split():
            if term_index.get(term) is None:
                continue
            lil[idx, term_index[term]] = 1
        # print(time, label)
    print('finish convert lil', path)
    with open(f'tmp/C/{ii:03d}.pkl', 'wb') as fp:
        pickle.dump((labels, lil[:len(labels)]), fp)
        # print(label, body)

args = [(ii, path) for ii, path in enumerate(sorted(Path().glob('tmp/B/*.csv')))]
#[pmap(arg) for arg in args]
with PPE(max_workers=4) as exe:
    exe.map(pmap, args)

