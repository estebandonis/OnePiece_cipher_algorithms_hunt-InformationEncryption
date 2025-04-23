import utils.zoro_rc4 as rc4

text = "6425eb738513a30c790862925ccac91193b9919cb8643451193b4c55dab9a2606329e81002"

key = "21610"

ciphertext_bytes = bytes.fromhex(text)

print(rc4.rc4_decrypt(ciphertext_bytes, key))