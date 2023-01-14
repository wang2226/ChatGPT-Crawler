#!/bin/bash

LOGFILE=log.txt

COMMANDS_LIST=("python pychatgpt.py --token xxx" "python pychatgpt.py --token hwang219" "python pychatgpt.py --token bai" "python pychatgpt.py --token bruce" )

change=`cat ./change_token`

writelog() {
  now=`date`
  echo "$now $*" >> $LOGFILE
}

writelog "Starting"

while true ; do
  for i in "${!COMMANDS_LIST[@]}"; do
    if [ "$change" = "True" ]; then
        echo "Change to the next token ..."
        sed -i 's/True/False/g' change_token
    fi
    ${COMMANDS_LIST[$i]}
  done

  writelog "Exited with status $?"
  writelog "Restarting"
done

echo "Finally finished!!"
