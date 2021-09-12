## main program base libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from contextlib import closing
import csv
import io
from datetime import datetime
import os
import threading
import time
import sys
from itertools import cycle
import netaddr
import resource as res


import pprint
import datetime as dt

## eos node libraries
import eospy.cleos
import eospy.keys
from eospy.types import Abi, Action
from eospy.utils import parse_key_file

## utils
import pytz
import json
import subprocess

## eos node ibraries
from eospy.cleos import Cleos
from prettytable import PrettyTable
import random
import config as conf



# Get random node
def randnode():
    lines = open('nodes').read().splitlines()
    myline =random.choice(lines)
    return (myline)


## send a message to a eos address

def send(options):
    addr = options[0]
    addr2 = options[1]
    msg = options[2]

    # encrypt data with reveicer public address
    #encrypted = encrypt(private_key, public_key, message)

    ce = eospy.cleos.Cleos(url=randomnode())

    arguments = {
        "from": addr,  # sender
        "to": addr2,  # receiver
        "quantity": '0.0001 EOS',  # In EOS
        "memo": msg,
    }
    payload = {
        "account": "eosio.token",
        "name": "transfer",
        "authorization": [{
            "actor": "eosio",
            "permission": "owner",
        }],
    }
# Converting payload to binary
    data = ce.abi_json_to_bin(payload['account'], payload['name'], arguments)
# Inserting payload binary form as "data" field in original payload
    payload['data'] = data['binargs']
# final transaction formed
    trx = {"actions": [payload]}
    trx['expiration'] = str(
        (dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
    key = eospy.keys.EOSKey(conf.privkey)
    try:
        resp = ce.push_transaction(trx, key, broadcast=True)
    except:
        pass
        print("ERROR - INVALID KEYS")


send([sys.argv[1],sys.argv[2],sys.argv[3]])
