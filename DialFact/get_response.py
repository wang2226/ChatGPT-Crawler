from chatgpt_wrapper import ChatGPT
import json
from tqdm import tqdm
import pandas as pd
from collections import defaultdict
import time
from datetime import datetime


VERSION = 0.2
TIMESTAMP = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


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
df = df.iloc[0:19]
print(df)
print(f"Length of df: {len(df)}")


bot = ChatGPT()

input = []
output = []

for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    query = row["response"]
    #query = "".join(i for i in row["context"]) + " " + row["response"]
    print(query)
    input.append(query)
    response = bot.ask(str(query))
    print(response)
    output.append(response)

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
    "version": VERSION,
    "created": TIMESTAMP,
    "result": result_list
}

with open(f"./processed/DialFact_{VERSION}.json", "w") as fp:
    json.dump(out, fp)
