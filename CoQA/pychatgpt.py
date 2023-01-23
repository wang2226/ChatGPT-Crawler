from pyChatGPT import ChatGPT
import json
from tqdm import tqdm
import pandas as pd
import time
from datetime import datetime
import numpy as np
import pickle
import argparse
import csv
import os
import sys


TIMESTAMP = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
DATASET = "CoQA"


# parser = argparse.ArgumentParser()
# parser.add_argument("--token", type=str, default="", help="token path")
# args = parser.parse_args()


if not os.path.exists(f"./start"):
    with open("./start", "w") as f:
        f.write(str(0))
        f.close()

with open("./start", "r") as f:
    start = f.read()
f.close()


raw_df = pd.read_pickle(f"./input_processed/{DATASET}.pkl")
end = raw_df.shape[0]
if start == 0:
    df = raw_df[int(start):end]
df = raw_df[int(start)+1:end]
print(df)

# try:
#     with open(f"./tokens/{args.token}", "r") as f:
#         token = f.read()
# except:
#     print("Cannot find valid tokens")
#     sys.exit(1)

token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..KR1wqFxWXikPl5PF.0i3AVLAafL-nPofFcMrMSvXajekyNGTVLVdpqvSqA_C41RvDZNaDW5hfjwS9ebzH38oJYERvRRxlq4MCTD-EFYXupeLHluggymIIYcfI0nyJ1f87_j3S26V4xYLHFjDVBvbhmZtci-lxSsMoUvRHL3CECaupmnMXQNmQVYllGzEcQgS7YkcLwlqUYK05M5YeLnZM_b2okX0bn8yjgOc97eUC_Jv_Qz2K6YrX4DREeuORccd61ii9ju-PoOxvdLpAWou1iNn7qot2igXtEBWm7DSGY7QegjqYolHLnw-pqiH4RFXljJHB2J8cCom2ncmFuK0kXKW8sRWyoSKHW4witOqfqp7-fSyXSPP3RzHchZ3lOGvU9SfbFPPMQAWJUtiznmkOkVdeZezx1Yq-6BplB6cfn2Wohl6ofLHKZ9N-lLzvmRh_fcfboixOsRSL04OUkO7tye4qApimLZyCHed7INWwpPzTWrjEsPnJCVwVKoNNFuIH9CK43jX0FSu8ySDkTOyWuJ2B_ZG-v5LbRo7BnKZShRcO_YRUazUXh1NDBjSRO8VZksQ-dTLsS-7vxEMJfPe-b3xNvTxKjA49B6o6KN3xko1PfHL15rILR3Q3YyNdJoKu-oJ1XhiQQD6BiC47q2Kd6RnB4M5s43H3VfI4wsnx1yt7HsavDP0kJf3HBS6d-deBvEnYWOhd6qP-trQ0Po0Vd2xxt7JgLDjei4gq_veUYzsfY33uLJlwntlc0ajUVB0zwP9D-wfE7GN2-5yWuuP8J2g7oSGKBC8Y6shjFYrAWOUbdWMYf9u78ZaaceVnhafeOM5nvo7ji6zuo41B0Z8-U4VZjBlbjhIlwpNwRgMluHFVlHjjrH5WeTMi_tsHNK7c1ZMiLYlOS_ZOAwhk3mvosaHpMzBwtZPf9EbVUF6iR085rPqrdV90PbZDOACQqNkAWwR4k2NdBFHx-SU427QQBoUyJDuieF0pQ_3dQxe3OSaA496ISWzGliLVmDqVN6biIiS373JTxtNVO1nCH6l-887E25s_Ce12UCaRzVQSDn_ZFSagF9BSQjfRoloF38LCP2NVEsovAkUW_DBDMF0ztx51qBfSEq1QfYsoRdfuugfW7qBC5cNVYRWzMDIGKxlH1ZLg3cSKvL9WTF2RUtkERY6hT_kSzx_ojn19dhI6oxj9uW0MnAchIA9QrvWUmEq8J7GCe3jG_nLkhnmebMntBY8BI-QEv5Q-Vxqp3h6sTQCWnkijKpt6dC_Dno5kqZWegShgAEvUa6d88sU6L8AXMajRMoKZ8WjEzV95XWeCDDOMaXeBBrM53qXt9a6CqKUTHhJs6lM2CtiingXC-I8M3vRXEWOxqmenCmDr-Augp0h1SIlJI404rr7jpeU-2-44ugSNq4GKwUkCi3zNIc2Mu14NVJ3WsApMW5Ipv4kEmsqtym5LZwzDAJ3hyJ3UNGC7gpUPXfVHjAU24CP_vT7l96mVXqzbGkXWAcPQN1s9eDRbV3sfJg-qTP2F1b44XTXrUWYxU6bFPRzWzUW1rLcxr5wtzePZ3OII4JXDk6ePTvaF6Ds7JQ08SuYg2NpXzQ_jDSvhROKCvox_BdAJezCGKF_31gsiVQD_czkZYT78B-CY1037q_d-DQIqUdPI7izqZtLANze5f6qgWJThNlD0JZ6FLq57VWBa9JkMdXvIWncBlhAm4zFzgKD4Vmp85o1hilT1wrgmi_Da1AKkWftogsO7s7gl5Bq9beMGB6q9r1d9RqdceN1tcj0TzmK3bUhkZ-naoBZNQSjPBYpgd4yHl3Yb2z_WcaXGOPAiswnLkmZ0DrvoVHyHTqfOj4ProgZortB9UujEAjWciR4tU6rnNVqOtT0yr-qfNJyn823stm182_hpehi4hJBZ2IIiXeOaCaTeDGB7oJiQhZRHBog-7T7znJxldbP-AJBLR9Ci5tO820sgVul6yi7bLKJucjDVZwYUaxNwn5wVMhk9iQ6OslXPzXMjfzdXK3KogsXwLlzYV3YXatZR5wxX0Yjmu0q_JDGfTP_f7adCsepCRZAkXJF272EpJyFnhXnVcYuZeuXyK4QkLPKt77-dSIKxtYOP_QNgbdmPftyNVmnByj-BRW5PNTD_W8Gk90gSeSaHKI4i4RC1RgfKPbkY_Bcz6nEyifbTdZKEUPUa5z6uOwo4_0wLk7M1A8ii_NjGrRzAO-UAg0K1yqVQ16t-ck8FzUN7GDWKyDRIBaY-9joz153emAWMi04JsKygt_ToZkQCDGblWzbdCG8AIg.Q3UKfDekVRHcR-DZf543ag"
session_token = token
api = ChatGPT(session_token)
# query= ''
# response = api.send_message(query)
# print(response["message"])

if not os.path.exists(f"./output_raw/{DATASET}_{int(start)}.csv"):
    f = open(f"./output_raw/{DATASET}_{int(start)}.csv", "w")
    f.close()


with open(f"./output_raw/{DATASET}_{int(start)}.csv", "a") as fp:
    writer = csv.writer(fp)
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        query = row["query"]

        print("*" * 20)
        print(query)
        print("*" * 20)

        try:
            response = api.send_message(query)
            print("=" * 20)
            print(response)
            print("=" * 20)

            if response["message"] != "":
                fields = [index, query, response["message"]]
                writer.writerow(fields)
            else:
                print(f"Stopped at: {index}")

            with open("./start", "w") as f:
                f.write(str(index))
            f.close()
        except ValueError as ve:
            print(ve)
            if str(ve) == "Too many requests in 1 hour. Try again later.":
                print(str(ve))
                f = open("change_token", "w")
                f.write("True")
                f.close()
            if str(ve) == "Only one message at a time. Please allow any other responses to complete before sending another message, or wait one minute.":
                print(str(ve))
                time.sleep(60)

fp.close()

# api.reset_conversation()  # reset the conversation
# api.clear_conversations()  # clear all conversations
# api.refresh_chat_page()  # refresh the chat page