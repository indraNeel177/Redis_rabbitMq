import pandas as pd

df = pd.read_csv("case2.csv")
df['RefLoc'] = df['RefLoc'].replace(22, "09")
# df['RefLoc'] = df['RefLoc'].replace(32, "09")
# del df['Unnamed: 9']

data = df.T.to_dict()

data_dict = []
for x in data:
    data_dict.append(data.get(x))

import json

with open('case2.json', 'w') as fp:
    json.dump(data_dict, fp)
