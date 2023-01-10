from chatgpt_wrapper import ChatGPT
import pandas as pd
import json
from tqdm import tqdm

# import json
# f = open('AQA_train.json')
# load_json = json.load(f)

context_paragraph = []
questions = []
answers = []
i=0

with open("./AQA_train.json") as f:
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





# bot = ChatGPT()
# response = bot.ask("What is 6 times 4?")
# print(response) 


