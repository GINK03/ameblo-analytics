
import pandas as pd
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor as PPE


def make_label(x):
    year = int(x.split('年')[0])
    if 1960 <= year < 1988:
        return 1
    if year >= 1988:
        return 0
    return None

def pmap(arg):
    path = arg
    print(path)
    
    df = pd.read_csv(path)
    df = df[pd.notnull(df['生年月日'])]
    df['label'] = df['生年月日'].apply(make_label)
    df = df[pd.notnull(df['label'])]
    df.to_csv(str(path).replace('/A/', '/B_generation/'), index=None)
args = [path for path in sorted(Path().glob('tmp/A/*.csv'))]
Path('tmp/B_generation').mkdir(exist_ok=True, parents=True)
[pmap(arg) for arg in args[0:1]]
with PPE(max_workers=8) as exe:
    exe.map(pmap, args)
