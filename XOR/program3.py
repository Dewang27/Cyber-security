import binascii
hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
byte_string = binascii.unhexlify(hex_string)
print(hex_string)
print(byte_string)

def xor_decrypt(byte_string, key):
    return ''.join(chr(b ^ key) for b in byte_string)

# Try all possible keys
for key in range(256):
    result = xor_decrypt(byte_string, key)
    print(f"Key: {key}, Result: {result}")

#cOOKINGmcSLIKEAPOUNDOFBACON