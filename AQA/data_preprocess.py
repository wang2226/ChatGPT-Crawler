from chatgpt_wrapper import ChatGPT
import numpy as np
import pandas as pd
import json
from tqdm import tqdm
import math


with open("./jsonl_files/convertjsoncombined.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=435):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][0]["question"])
        answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

    df0= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convertjsoncombined.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][1]["question"])
        answers.append(l["paragraphs"][0]["qas"][1]["answers"][0]["text"])

    df1= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convertjsoncombined.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][2]["question"])
        answers.append(l["paragraphs"][0]["qas"][2]["answers"][0]["text"])

    df2= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convert_AQA.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][0]["question"])
        answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

    df3= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convert_AQA.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][1]["question"])
        answers.append(l["paragraphs"][0]["qas"][1]["answers"][0]["text"])

    df4= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convertjson0.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][0]["question"])
        answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

    df5= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convertjson2.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][0]["question"])
        answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

    df7= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convertjson3.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][0]["question"])
        answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

    df8= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convertjson5.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][0]["question"])
        answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

    df10= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])

with open("./jsonl_files/convertjson7.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][0]["question"])
        answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

    df12= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                    "title", "context", "question", "answers"])



df = pd.concat([df0, df1, df2, df3, df4, df5, df7, df8, df10, df10, df12])
df["query"] = df["context"].astype(str) + " " + df["question"].astype(str)
df = df.astype(str).drop_duplicates(["query"]).reset_index(drop=True)
df = df.iloc[:2001,:]
print(df)

df.to_csv("CoQA_data_aqa.csv", index=False)

# df.to_pickle(f"./input_processed/{DATASET}.pkl")
# print(df.head)
# df.to_csv('file6.csv')


# def chunking_dataset(CHUNK):
#     num_chunks = math.ceil(df.shape[0] / CHUNK)
#     df_list = np.array_split(df, num_chunks)

#     total = 0
#     for i in range(len(df_list)):
#         total = total + len(df_list[i])
#         df_list[i].to_pickle(f"./AQA/preprocess/{i}.pkl")

#     print(f"Total: {total}")

# chunking_dataset(CHUNK=50)


