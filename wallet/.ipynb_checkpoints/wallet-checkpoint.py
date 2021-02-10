from constants import *
from dotenv import load_dotenv
import os
import subprocess
import json


#mnemonic = "ramp stomach hotel sun craft traffic huge cage auction inspire narrow produce shock boss surge"
#def derive_wallets()
command = './derive -g --mnemonic="ramp stomach hotel sun craft traffic huge cage auction inspire narrow produce shock boss surge" --cols=path,address,privkey,pubkey --coin=BTC --Numderive=3 --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
