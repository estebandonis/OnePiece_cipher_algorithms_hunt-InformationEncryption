import utils.luffy_xor as luffy

text = "747d77766f5009065408025503550354080602030701500853060306500402040104070a55"

key = "21610"

# Convert hex string to bytes
text_bytes = bytes.fromhex(text)

byteFlag = luffy.xor_cipher(text_bytes, key)

print(''.join(chr(b) if 32 <= b <= 126 else '.' for b in byteFlag))