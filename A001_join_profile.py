from pathlib import Path
import pandas as pd

dfs = []
for path in Path().glob('../tmp/ameblo_jsons_profile_*.csv'):
    print(path)
    df = pd.read_csv(path)
    dfs.append(df)
df = pd.concat(dfs, axis=0)
df.to_csv('tmp/profile.csv', index=None)
