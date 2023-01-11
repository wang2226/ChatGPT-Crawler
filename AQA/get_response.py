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
import argparse


TIMESTAMP = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
DATASET = "AQA"
CHUNK = 50


df = pd.read_pickle(f"./AQA/preprocess/0.pkl")


# for index, row in tqdm(df.iterrows(), total=df.shape[0]):
#     #query = row["response"]
#     query = "".join(i for i in row["context"]) + " " + row["question"]

#     print("*" * 20)
#     print(query)
#     print("*" * 20)
#     # input.append(query)


# parser = argparse.ArgumentParser()
# parser.add_argument("--part", type=int, default=0, help="which part of dataset")
# args = parser.parse_args()

# part = args.part
# df = pd.read_pickle(f"./preprocess/{part}.pkl")
# print(df)

bot = ChatGPT()

input = []
output = []

for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    #query = row["response"]
    query = "".join(i for i in row["context"]) + " " + row["question"]

    # print("*" * 20)
    # print(query)
    # print("*" * 20)
    input.append(query)

    response = bot.ask(str(query))
    print("=" * 20)
    print(response)
    print("=" * 20)

    output.append(response)

    if response == "Unusable response produced by ChatGPT, maybe its unavailable.":
        break

# result = pd.DataFrame(list(zip(input, output)), columns=["input", "output"])
# result.to_csv("./result.csv", sep="\t", encoding="utf-8")

result_list = []
for i in range(df.shape[0]):
    result_list.append({
        "input": input[i],
        "output": output[i]
    })

out = defaultdict(lambda: defaultdict(lambda: {}))
out = {
    "author": "IIT",
    "dataset": DATASET,
    "part": part,
    "created": TIMESTAMP,
    "result": result_list
}

with open(f"./processed/DialFact_{part}.json", "w") as fp:
    json.dump(out, fp)