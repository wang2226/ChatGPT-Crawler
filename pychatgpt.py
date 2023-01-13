from pyChatGPT import ChatGPT
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
import csv
import os


TIMESTAMP = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
DATASET = "DialFact"


parser = argparse.ArgumentParser()
parser.add_argument("--token", type=str, default=0, help="token path")
args = parser.parse_args()


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


with open("./start.txt", "r") as f:
    start = f.read()
f.close()

#raw_df = pd.concat([df_valid, df_test])
raw_df = df_valid
end = raw_df.shape[0]
if start == 0:
    df = raw_df[int(start):end]
df = raw_df[int(start)+1:end]
print(df)


with open(f"./{args.token}", "r") as f:
    token = f.read()

session_token = token  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)  # auth with session token
# api = ChatGPT(session_token, conversation_id="some-random-uuid")  # specify conversation id
# api = ChatGPT(session_token, proxy="https://proxy.example.com:8080")  # specify proxy
# api = ChatGPT(session_token, chrome_args=["--window-size=1920,768"])  # specify chrome args
#api = ChatGPT(session_token, moderation=False)  # disable moderation
#api = ChatGPT(session_token, verbose=True)  # verbose mode (print debug messages)


if not os.path.exists(f"./processed/DialFact_{int(start)}.csv"):
    f = open(f"./processed/DialFact_{int(start)}.csv", "w")
    f.close()


with open(f"./processed/DialFact_{int(start)}.csv", "a") as fp:
    writer = csv.writer(fp)
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        #query = row["response"]
        query = "".join(i for i in row["context"]) + " " + row["response"]

        print("*" * 20)
        print(query)
        print("*" * 20)

        try:
            response = api.send_message(query)
            print(response)
            print("=" * 20)
            print(response["message"])
            print("=" * 20)

            if response["message"] != "":
                fields = [index, query, response["message"]]
                writer.writerow(fields)
            else:
                print(f"Stopped at: {index}")

            with open("./start.txt", "w") as f:
                f.write(str(index))
            f.close()
        except ValueError as ve:
            time.sleep(60)

fp.close()

api.reset_conversation()  # reset the conversation
api.clear_conversations()  # clear all conversations
api.refresh_chat_page()  # refresh the chat page