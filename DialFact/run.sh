#!/bin/bash

DIR=./preprocess/*.pkl

for file in $DIR; 
do
	python get_response.py --part "$(basename ${file%.*})"
	sleep 3600
done
