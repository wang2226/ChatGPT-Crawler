import numpy as np
import pandas as pd
import math

data_og = pd.read_pickle("./FaVIQ_original.pkl")
data = pd.read_pickle("./FaVIQ.pkl")
print(data_og.head())

print(len(data_og))
print(len(data))
# print('*'*40)
# print(data_og.head())

# # data_last = data_og.iloc[-1002:]

# df_diff = pd.concat([data_og['query'],data['input']]).drop_duplicates(keep='first')
# print(df_diff)

# outputs = []
# for i in data['output']:
#     str = i[0:1]
#     outputs.append(str)
# data['new_output'] = outputs

df3 = pd.merge(data_og, data, how='inner', left_on='question', right_on='input')
df3.to_csv("data_new_faviq.csv", index=True)





