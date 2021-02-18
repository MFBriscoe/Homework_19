key = wif_to_key("miLvzXGQhLriDpamjMGysMBNdgN6Lc3xxh")

to_address = ["mvKKAkXMSm39n4Roz6yXpUk7bsESuk81W1"]

outputs = []

for address in addresses:
    outputs.append((address, 0.0001, "btc-test"))

print(key.send(outputs))