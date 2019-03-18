import pandas as pd
from pathlib import Path
import MeCab
from concurrent.futures import ProcessPoolExecutor as PPE
m = MeCab.Tagger('-Owakati')

dfP = pd.read_csv('tmp/profile.csv')
def pmap(arg):
    idx, path = arg
    print(path)
    df = pd.read_csv(path)
    

    objs = []
    for obj in df.to_dict('record'):
        try:
            obj['body'] = m.parse(str(obj['body'])).strip()
            obj['title'] = m.parse(str(obj['title'])).strip()
            obj['user'] = obj['canonical'].split('/')[-2]
            # print(obj['user'])
        except Exception as ex:
            print(ex)
            continue
        objs.append(obj)
    dfR = pd.DataFrame(objs)
    dfR = dfR.join(dfP.set_index('user'), on='user')
    dfR.to_csv(f'tmp/A/{idx:03d}.csv', index=None)


Path('tmp/A').mkdir(exist_ok=True, parents=True)
args = [(idx, path) for idx, path in enumerate(
    sorted(Path('../tmp').glob('ameblo_jsons_content_*.csv')))]
#[pmap(arg) for arg in args]
with PPE(max_workers=8) as exe:
    exe.map(pmap, args)
