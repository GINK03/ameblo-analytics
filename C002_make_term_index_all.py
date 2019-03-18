import pandas as pd
from pathlib import Path
import json

doc_freq = {}
for path in sorted(Path().glob('tmp/B/*.csv')):
    print(path)
    df = pd.read_csv(path)
    df = df[['label', 'body']]
    for body in df['body']:
        for term in set(str(body).split()):
            if doc_freq.get(term) is None:
                doc_freq[term] = 0
            doc_freq[term] += 1
json.dump(doc_freq,fp=open('tmp/doc_freq.json', 'w'), indent=2, ensure_ascii=False)

term_index = {}
for path in sorted(Path().glob('tmp/B/*.csv')):
    print(path)
    df = pd.read_csv(path)
    df = df[['label', 'body']]
    for body in df['body']:
        for term in set(str(body).split()):
            if term_index.get(term) is None:
                term_index[term] = len(term_index)
json.dump(term_index,fp=open('tmp/term_index.json', 'w'), indent=2, ensure_ascii=False)
