from chatgpt_wrapper import ChatGPT
import pandas as pd
import json
from tqdm import tqdm

with open("./convert_AQA.jsonl") as f:
    title, paragraph_id, context, question, answers = [], [], [], [], []
    for line in tqdm(f, total=2):
        l = json.loads(line)
        # print(l)
        # if l["data_type"] == "written" and l["type_label"] == "factual":
        title.append(l["title"])
        # paragraph_id.append(l["paragraphs"])
        context.append(l["paragraphs"][0]["context"])
        question.append(l["paragraphs"][0]["qas"][0]["question"])
        answers.append(l["paragraphs"][0]["qas"][0]["answers"][0]["text"])
            # type_label.append(l["type_label"])

    df= pd.DataFrame(list(zip(title, context, question, answers)), columns=[
                      "title", "context", "question", "answers"])


print(df.head)
df.to_csv('file1.csv')


# bot = ChatGPT()
# response = bot.ask("What is 6 times 4?")
# print(response) 


