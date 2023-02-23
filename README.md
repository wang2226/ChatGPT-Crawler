# ChatGPT Crawler

This script automates the process sending a query to ChatGPT and saves the response.
Since the release of Dec 15th version, ChatGPT has imposed hourly limit per account.
To solve this, this script takes multiple accounts (I found the minimum to be 4), rotates and exhausts the hourly limit of each account.

In order to register an OpenAI account, you need an email and a phone number for verification. Note that it has to be a real phone number. Bummer! I tried to register accounts with Google Voice virtual phone number, OpenAI recognized it being a virtual number and wouldn't let me register.

Note: This code is built on top of [pyChatGPT](https://github.com/terry3041/pyChatGPT). 

## Installation

1. Please follow installation instruction from [pyChatGPT](https://github.com/terry3041/pyChatGPT)

2. Creates the following folders:

```sh
mkdir ./input_raw
mkdir ./input_processed
mkdir ./output_raw
mkdir ./output_processed
mkdir ./tokens
```

## Run

1. Save the tokens (a.k.a. `__Secure-next-auth.session-token`) as files under `./tokens` folder.
2. Modify `preprocess.py` to process the raw dataset. The end goal is to save the processed dataset as a Pandas Dataframe object, with a column named `query` that contains the queries to feed to ChatGPT.
3. Change `DATASET` variable in `pychatgpt.py`.
4. Start the script `./run.sh`.
