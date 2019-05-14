
import pandas as pd
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor as PPE

def pmap(arg):
    path = arg
    print(path)
    
    df = pd.read_csv(path)
    df = df[pd.notnull(df['居住地'])]
    df['label'] = df['居住地'].apply(lambda x:1 if x == '東京都' else 0)
    df.to_csv(str(path).replace('/A/', '/B_location/'), index=None)
args = [path for path in Path().glob('tmp/A/*.csv')]
Path('tmp/B_location').mkdir(exist_ok=True, parents=True)
[pmap(arg) for arg in args[0:1]]
with PPE(max_workers=8) as exe:
    exe.map(pmap, args)
