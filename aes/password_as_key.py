import requests
import tqdm
from Crypto.Cipher import AES
import hashlib
from Crypto.Util.number import *
import tqdm
import random
import binascii
result = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ciphertexthex=result.json() ["ciphertext"]
# print(ciphertext_hex)
# ciphertexthex='c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'
with open("C:\\DewangData\\VSCode\\Projects\\PYTHON WS\\aes\\words.txt", 'r') as f:
    words = f.read()
    words=words.strip()
    # print(words)
    key_1 = hashlib.md5(words.encode()).hexdigest()
    key=bytes.fromhex(key_1)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = bytes.fromhex(ciphertexthex)
    decrypted = cipher.decrypt (ciphertext)
    if b'crypto{' in decrypted:
        print(decrypted)
    print(decrypted)
