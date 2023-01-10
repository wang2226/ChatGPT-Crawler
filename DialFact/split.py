from chatgpt_wrapper import ChatGPT
import json
from tqdm import tqdm
import pandas as pd
from collections import defaultdict
import time
from datetime import datetime
import numpy as np
from math import ceil
import pickle


TIMESTAMP = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
DATASET = "DialFact"
CHUNK = 50

with open("./raw/valid_split.jsonl") as f:
    context_id, id, context, response, response_label, type_label = [], [], [], [], [], []
    for line in tqdm(f, total=10436):
        l = json.loads(line)
        if l["data_type"] == "written" and l["type_label"] == "factual":
            context_id.append(l["context_id"])
            id.append(l["id"])
            context.append(l["context"])
            response.append(l["response"])
            response_label.append(l["response_label"])
            type_label.append(l["type_label"])

    df_valid = pd.DataFrame(list(zip(context_id, id, context, response, response_label, type_label)), columns=[
                      "context_id", "id", "context", "response", "response_label", "type_label"])
    #print(df_valid)


with open("./raw/test_split.jsonl") as f:
    context_id, id, context, response, response_label, type_label = [], [], [], [], [], []
    for line in tqdm(f, total=11809):
        l = json.loads(line)
        if l["data_type"] == "written" and l["type_label"] == "factual":
            context_id.append(l["context_id"])
            id.append(l["id"])
            context.append(l["context"])
            response.append(l["response"])
            response_label.append(l["response_label"])
            type_label.append(l["type_label"])

    df_test = pd.DataFrame(list(zip(context_id, id, context, response, response_label, type_label)), columns=[
                      "context_id", "id", "context", "response", "response_label", "type_label"])
    #print(df_test)


df = pd.concat([df_valid, df_test])
num_chunks = ceil(df.shape[0] / CHUNK)
df_list = np.array_split(df, num_chunks)

total = 0
for i in range(len(df_list)):
    total = total + len(df_list[i])
    df_list[i].to_pickle(f"./preprocess/{i}.pkl")

print(f"Total: {total}")