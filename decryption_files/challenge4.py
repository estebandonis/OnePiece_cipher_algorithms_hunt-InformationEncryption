import utils.nami_chacha as nami

text = "3fc06ae08a46a3bcdfd26cda042230506336e03e26d653ae9948f7c3b2638e3a653cec5536"

key = "21610"

print(nami.chacha20_decrypt(bytes.fromhex(text), key))
