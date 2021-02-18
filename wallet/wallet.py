from constants import *
from dotenv import load_dotenv
import os
import subprocess
import json
from pprint import pprint
from web3 import Web3
from bit import wif_to_key
from web3.middleware import geth_poa_middleware
from eth_account import Account

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

#mnemonic = "ramp stomach hotel sun craft traffic huge cage auction inspire narrow produce shock boss surge"

mnemonic = os.getenv('MNEMONIC', 'ramp stomach hotel sun craft traffic huge cage auction inspire narrow produce shock boss surge')

def derive_wallets(coin, Numderive):
    command = f'./derive -g --mnemonic="{mnemonic}" --coin={coin} --numderive={Numderive} --cols=path,address,privkey,pubkey --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

print(derive_wallets(BTC, 3))
coins = {ETH: derive_wallets(ETH, 3), BTCTEST: derive_wallets(BTCTEST, 3)}
pprint(coins)

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin ==BTCTEST:
        return PrivateKeyTestnet(priv_key)

def create_tx(coin, account, address_to, amount):
    if coin ==ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account,
             "to": address_to,
             "value": amount}
        )
        return {
        'from': account.address,
        'to': address_to,     
        'value': amount, 
        'gas': w3.eth.gasPrice, 
        'gasPrice': gasEstimate, 
        'nonce': w3.eth.getTransactionCount(account.address),
        'chainID': 2424}
    if coin ==BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, to, amount):
    if coin ==ETH:
        raw_tx=create_tx(coin, account, to, amount)
        signed= account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    if coin ==BTCTEST:
        raw_tx=create_tx(coin, account, to, amount)
        signed= account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)

    
    
#key = wif_to_key("cVJFcCsEaV13VfcbxeWD3zoDenqzVW7oGQkJHWK5tro88zsE9iwz")

#to_address = ["mvKKAkXMSm39n4Roz6yXpUk7bsESuk81W1"]

#outputs = []

#for address in to_address:
#    outputs.append((address, 0.0001, "btc"))

#print(key.send(outputs))


#send_tx(ETH, account, Web3.toChecksumAddress("0xF7788597890a85c2b78782d877B89A8339361b5F"), 8888)