
import pandas as pd
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor as PPE

def pmap(arg):
    path = arg
    print(path)
    
    df = pd.read_csv(path)
    df = df[pd.notnull(df['性別'])]
    #df['time'] = pd.to_datetime(df['time'])
    #lower = pd.to_datetime('2019-01-01')
    df['label'] = df['性別'].apply(lambda x:1 if x == '女性' else 0)
    df.to_csv(str(path).replace('/A/', '/B_gender/'), index=None)
args = [path for path in Path().glob('tmp/A/*.csv')]
Path('tmp/B_gender').mkdir(exist_ok=True, parents=True)
#[pmap(arg) for arg in args]
with PPE(max_workers=8) as exe:
    exe.map(pmap, args)
