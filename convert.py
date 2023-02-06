import numpy as np
import pandas as pd
import math

data = pd.read_csv("./DialFact_original.csv")
data_og = pd.read_csv("./DialFact_result.csv")
# print(data.head())

# print('*'*40)
# print(data_og.head())

# # data_last = data_og.iloc[-1002:]

df_diff = pd.concat([data_og['input'],data['query']]).drop_duplicates(keep=False)
print(df_diff)

outputs = []
for i in data_og['output']:
    outputs.append(i)




data['chatgpt_response'] = outputs
del data['context_id']
del data['id']
del data['query']
del data['response_label']
del data['type_label']


data.to_csv("DialFact_withResponse.csv", index=True)


# context + question + answer
# context + question + chatgpt response


