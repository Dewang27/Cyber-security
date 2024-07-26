import binascii

def single_byte_xor_encryption(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext

plaintext="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key="ICE"
ciphertext = single_byte_xor_encryption(plaintext, key)
print(ciphertext)
hex_ciphertext=binascii.hexlify(ciphertext.encode())
print(hex_ciphertext)

