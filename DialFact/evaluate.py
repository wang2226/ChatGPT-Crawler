import json
import pandas as pd

name = "DialFact_1.2.json"

with open(f"./processed/{name}") as f:
    input, output = [], []
    for line in f:
        l = json.loads(line)
        for i in range(len(l["result"])):
            input.append(l["result"][i]["input"])
            output.append(l["result"][i]["output"])

df = pd.DataFrame(list(zip(input, output)), columns=["input", "output"])
print(df)

