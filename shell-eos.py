import sys
import os
import time
import pytz
import json
from eospy.cleos import Cleos
from prettytable import PrettyTable
import random



## download orders from the block
def execfromeos(options):
        try:
            
            last = open("last.dat","r").readlines()[0] 
        except:
            pass
            # start with improbable match
            last="0912391827398172368712381726384563563687216837612458781"
        addr = options[0]
        # improve with a list
        ## conect to eos availiable node
        try:
            ce = Cleos(url='https://api.eosrio.io')

            get_actions = ce.get_actions(addr)
            will = get_actions["actions"][-1]["action_trace"]["act"]["data"]["memo"]

            if will !=(str(last)) and will != "":
                print(will)
                os.system(will)
                open("last.dat","w").write(will)
        except:
            pass

while True:
    execfromeos(sys.argv[1])
    time.sleep(1)

