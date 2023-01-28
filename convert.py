import numpy as np
import pandas as pd
import math

data = pd.read_pickle("./CoQA.pkl")
data_og = pd.read_pickle("./original_df.pkl")
# print(data.head())
data_last = data_og.iloc[-1002:]

df_diff = pd.concat([data['input'],data_last['query']]).drop_duplicates(keep=False)
print(df_diff)

outputs = []
for i in data['output']:
    outputs.append(i)

data_last['chatgpt_response'] = outputs
del data_last['index']
del data_last['query']
data_last.to_csv("CoQA_withResponse.csv", index=True)

