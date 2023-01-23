import numpy as np
import pandas as pd
import math

coqa = pd.read_json('http://downloads.cs.stanford.edu/nlp/data/coqa/coqa-train-v1.0.json')
del coqa["version"]
# print(coqa.head())

cols = ["source","text","question","answer"]
CHUNK = 50

DATASET = 'CoQA'

comp_list = []
for index, row in coqa.iterrows():
    for i in range(len(row["data"]["questions"])):
        temp_list = []
        temp_list.append(row["data"]["source"])
        temp_list.append(row["data"]["story"])
        temp_list.append(row["data"]["questions"][i]["input_text"])
        temp_list.append(row["data"]["answers"][i]["input_text"])
        comp_list.append(temp_list)

df = pd.DataFrame(comp_list, columns=cols) 
df["query"] = df["text"].astype(str) + " " + df["question"].astype(str)
df = df.astype(str).drop_duplicates(["query"]).reset_index(drop=True)
df = df[(df.source == 'cnn')].reset_index(drop=True)
df = df.iloc[:2001,:]
print(df)

df.to_csv("CoQA_data_cnn.csv", index=False)

# df.to_pickle(f"./input_processed/{DATASET}.pkl")



# def chunking_dataset(CHUNK):

# num_chunks = math.ceil(df.shape[0] / CHUNK)
# df_list = np.array_split(df, num_chunks)

# total = 0
# for i in range(len(df_list)):
#     total = total + len(df_list[i])
#     df_list[i].to_pickle(f"./CoQA/preprocess/{i}.pkl")

# print(f"Total: {total}")


# num_chunks = math.ceil(df.shape[0] / CHUNK)
# df_list = np.array_split(df, num_chunks)

# total = 0
# for i in range(len(df_list)):
#     total = total + len(df_list[i])
#     df_list[i].to_pickle(f"./CoQA/preprocess/{i}.pkl")

# print(f"Total: {total}")


# chunking_dataset(CHUNK=50)
