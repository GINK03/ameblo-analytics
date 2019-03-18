
import pandas as pd
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor as PPE

def pmap(arg):
    path = arg
    print(path)
    
    df = pd.read_csv(path)
    #df['time'] = pd.to_datetime(df['time'])
    #lower = pd.to_datetime('2019-01-01')
    df['label'] = df['time'].apply(lambda x:1 if x >= '2019-01-01' else 0)
    df.to_csv(str(path).replace('/A/', '/B/'), index=None)
args = [path for path in Path().glob('tmp/A/*.csv')]
Path('tmp/B').mkdir(exist_ok=True, parents=True)
#[pmap(arg) for arg in args]
with PPE(max_workers=8) as exe:
    exe.map(pmap, args)
