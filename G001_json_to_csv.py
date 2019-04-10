import json
import pandas as pd
import glob
import re
from pathlib import Path

Path('tmp/last_data/').mkdir(exist_ok=True)
for fn in glob.glob('tmp/term_weight_*.json'):
    typeof = re.search(r'\d_(.*?).json$', fn).group(1)
    print(typeof)
    df = pd.DataFrame(json.load(open(fn)))
    df.columns = ['feat', 'weight']

    df = df.sort_values(by=['weight'], ascending=True)
    df.head(50).to_csv(f'tmp/last_data/{typeof}_asc.csv', index=None)
    
    df = df.sort_values(by=['weight'], ascending=False)
    df.head(50).to_csv(f'tmp/last_data/{typeof}_dec.csv', index=None)
