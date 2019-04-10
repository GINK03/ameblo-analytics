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
Path('tmp/C_generation').mkdir(exist_ok=True)

def pmap(arg):
    ii, path = arg
    print(path)
    df = pd.read_csv(path)
    df = df[['time', 'label', 'body']]
    labels = []
    lil  = Lil((len(df), len(term_index),))
    for idx, (time, label, body) in enumerate(zip(df['time'], df['label'], df['body'])):
        labels.append(label)
        for term in str(body).split():
            if term_index.get(term) is None:
                continue
            lil[idx, term_index[term]] = 1
    print('finish convert lil', path)
    with open(f'tmp/C_generation/{ii:03d}.pkl', 'wb') as fp:
        pickle.dump((labels, lil[:len(labels)]), fp)

args = [(ii, path) for ii, path in enumerate(sorted(Path().glob('tmp/B_generation/*.csv')))]
[pmap(arg) for arg in args[0:1]]
with PPE(max_workers=6) as exe:
    exe.map(pmap, args)

