import pandas as pd
import numpy as np

import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer


def data_processing_coqa(dataset):

    coqa = pd.read_json(dataset)
    del coqa["version"]
    coqa_columns = ["text","question","answer"]
    new_data_list = []
    for index, row in coqa.iterrows():
        for i in range(len(row["data"]["questions"])):
            temp = []
            temp.append(row["data"]["story"])
            temp.append(row["data"]["questions"][i]["input_text"])
            temp.append(row["data"]["answers"][i]["input_text"])
            new_data_list.append(temp)
    coqa_new = pd.DataFrame(new_data_list, columns=coqa_columns)
    return coqa_new.to_csv("CoQA_dataset.csv", index=False)

# data_processing_coqa('http://downloads.cs.stanford.edu/nlp/data/coqa/coqa-train-v1.0.json')
# data = pd.read_csv("CoQA_dataset.csv")

load_model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')


def evaluating_QA(question, text):
    input_ids = tokenizer.encode(question, text)
    tokens = tokenizer.convert_ids_to_tokens(input_ids)
    seq_count = input_ids.index(tokenizer.sep_token_id)
    num_seg_a = seq_count+1
    num_seg_b = len(input_ids) - num_seg_a
    segment_ids = [0]*num_seg_a + [1]*num_seg_b
    assert len(segment_ids) == len(input_ids)
    
    output = load_model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]))
    
    answer_start = torch.argmax(output.start_logits)
    answer_end = torch.argmax(output.end_logits)

    if answer_end >= answer_start:
        answer = tokens[answer_start]
        for i in range(answer_start+1, answer_end+1):
            if tokens[i][0:2] == "##":
                answer += tokens[i][2:]
            else:
                answer += " " + tokens[i]
                
    if answer.startswith("[CLS]"):
        answer = "Unable to find the answer to your question."
    print("\nAnswer:\n{}".format(answer.capitalize()))


text = """New York (CNN) -- More than 80 Michael Jackson collectibles -- including the late pop star's famous rhinestone-studded glove from a 1983 performance -- were auctioned off Saturday, reaping a total $2 million. Profits from the auction at the Hard Rock Cafe in New York's Times Square crushed pre-sale expectations of only $120,000 in sales. The highly prized memorabilia, which included items spanning the many stages of Jackson's career, came from more than 30 fans, associates and family members, who contacted Julien's Auctions to sell their gifts and mementos of the singer. Jackson's flashy glove was the big-ticket item of the night, fetching $420,000 from a buyer in Hong Kong, China. Jackson wore the glove at a 1983 performance during \"Motown 25,\" an NBC special where he debuted his revolutionary moonwalk. Fellow Motown star Walter \"Clyde\" Orange of the Commodores, who also performed in the special 26 years ago, said he asked for Jackson's autograph at the time, but Jackson gave him the glove instead. "The legacy that [Jackson] left behind is bigger than life for me,\" Orange said. \"I hope that through that glove people can see what he was trying to say in his music and what he said in his music.\" Orange said he plans to give a portion of the proceeds to charity. Hoffman Ma, who bought the glove on behalf of Ponte 16 Resort in Macau, paid a 25 percent buyer's premium, which was tacked onto all final sales over $50,000. Winners of items less than $50,000 paid a 20 percent premium."""
question = "Where was the Auction held?"

evaluating_QA(question, text)

