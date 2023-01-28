import numpy as np
import pandas as pd
import tensorflow as tf
import transformers
from train_BERT import DataLoader

load_model = tf.keras.models.load_model('./sematic-similarity.h5')

def check_similarity(sentence1, sentence2):
    sentences = np.array([[str(sentence1), str(sentence2)]])
    test_data = DataLoader(sentences, labels=None, batch_size=1, shuffle=False, include_labels=False)

    proba = load_model.predict(test_data[0])[0]
    idx = np.argmax(proba)
    proba = f"{proba[idx]: .2f}%"
    # pred = labels[idx]
    # print(pred)
    # print(proba)
    return proba, sentence1, sentence2

df = pd.read_csv('../CoQA_withResponse.csv')
df["answer_prompt"] = df["text"].astype(str) + " " + df["question"].astype(str) + " The answer is "+ df["answer"].astype(str)
df["chatgpt_prompt"] = df["text"].astype(str) + " " + df["question"].astype(str) + " The answer is "+ df["chatgpt_response"].astype(str)

answer_prompt = []
for i in df['answer_prompt']:
    answer_prompt.append(i)

chatgpt_prompt = []
for j in df['chatgpt_prompt']:
    chatgpt_prompt.append(i)

similarity_p=[]
for i, j in zip(answer_prompt, chatgpt_prompt):
    similarity = check_similarity(i, j)[0]
    print(similarity)
    similarity_p.append(similarity)


df["BERT similarity"] = similarity_p

df.to_csv("CoQA_withGoldenR.csv", index=True)
