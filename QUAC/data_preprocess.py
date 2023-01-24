from chatgpt_wrapper import ChatGPT
import numpy as np
import pandas as pd
import json
from tqdm import tqdm
import math
# from general_utils import flatten_json, normalize_text, build_embedding, load_glove_vocab, pre_proc, get_context_span, find_answer_span, feature_gen, token2id
# coqa = 'https://s3.amazonaws.com/my89public/quac/val_v0.2.json'
coqa = './val_v0.2.json'

def flatten_json(file, proc_func):
    with open(file, encoding="utf8") as f:
        data = json.load(f)['data']
    rows, contexts = [], []
    for i in range(len(data)):
        partial_rows, context = proc_func(i, data[i])
        rows.extend(partial_rows)
        contexts.append(context)
    return rows, contexts

def proc_train(ith, article):
    rows = []
    
    for paragraph in article['paragraphs']:
        context = paragraph['context']
        for qa in paragraph['qas']:
            question = qa['question']
            answers = qa['orig_answer']
            answer = answers['text']

            rows.append((context, question, answer))
    return rows, context

train, train_context = flatten_json(coqa, proc_train)
df = pd.DataFrame(train, columns=['context', 'question', 'answer',])
df["query"] = df["context"].astype(str) + ". " + df["question"].astype(str)
df = df.astype(str).drop_duplicates(["query"]).reset_index(drop=True)
df = df.iloc[:2001,:]
print(df)

df.to_csv("QUAC_data.csv", index=False)


