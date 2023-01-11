from chatgpt_wrapper import ChatGPT
import pandas as pd
import json
from tqdm import tqdm

with open("./convertjsoncombined.jsonl") as f:
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

with open("./convertjsoncombined.jsonl") as f:
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


with open("./convertjsoncombined.jsonl") as f:
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


with open("./convert_AQA.jsonl") as f:
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

with open("./convert_AQA.jsonl") as f:
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


with open("./convertjson0.jsonl") as f:
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


# with open("./convertjson1.jsonl") as f:
#     title, paragraph_id, context, question, answers = [], [], [], [], []
#     for line in tqdm(f, total=2):
#         l = json.loads(line)
#         # print(l)
#         title.append(l["title"])
#         # paragraph_id.append(l["paragraphs"])
#         context.append(l["paragraphs"][0]["context"])
#         question.append(l["paragraphs"][0]["qas"][0]["question"])
#         answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

#     df6= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
#                       "title", "context", "question", "answers"])



with open("./convertjson2.jsonl") as f:
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


with open("./convertjson3.jsonl") as f:
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



# with open("./convertjson4.jsonl") as f:
#     title, paragraph_id, context, question, answers = [], [], [], [], []
#     for line in tqdm(f, total=2):
#         l = json.loads(line)
#         # print(l)
#         title.append(l["title"])
#         # paragraph_id.append(l["paragraphs"])
#         context.append(l["paragraphs"][0]["context"])
#         question.append(l["paragraphs"][0]["qas"][0]["question"])
#         answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

#     df9= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
#                       "title", "context", "question", "answers"])



with open("./convertjson5.jsonl") as f:
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



# with open("./convertjson6.jsonl") as f:
#     title, paragraph_id, context, question, answers = [], [], [], [], []
#     for line in tqdm(f, total=2):
#         l = json.loads(line)
#         # print(l)
#         title.append(l["title"])
#         # paragraph_id.append(l["paragraphs"])
#         context.append(l["paragraphs"][0]["context"])
#         question.append(l["paragraphs"][0]["qas"][0]["question"])
#         answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

#     df11= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
#                       "title", "context", "question", "answers"])



with open("./convertjson7.jsonl") as f:
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




# with open("./convertjson0.jsonl") as f:
#     title, paragraph_id, context, question, answers = [], [], [], [], []
#     for line in tqdm(f, total=2):
#         l = json.loads(line)
#         # print(l)
#         title.append(l["title"])
#         # paragraph_id.append(l["paragraphs"])
#         context.append(l["paragraphs"][0]["context"])
#         question.append(l["paragraphs"][0]["qas"][0]["question"])
#         answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])

#     df5= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
#                       "title", "context", "question", "answers"])


df = pd.concat([df0, df1, df2, df3, df4, df5, df7, df8, df10, df10, df12])
df.drop_duplicates(['question'])
# print(df.head)
df.to_csv('file6.csv')


# bot = ChatGPT()
# response = bot.ask("What is 6 times 4?")
# print(response) 


