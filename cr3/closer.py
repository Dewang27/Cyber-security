

import os, json, random, math
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import getPrime, GCD, isPrime
from hashlib import sha256

def decrypt(g):
    out = {'iv': '6f69ac380715dbf9b00ef32ca8c204bb', 'ct': 'e654237a76d61d3bf97b315af1c2a517797b34b8eca270dbc8132dda1f425065b7b84690d4c21cdaf2ab17c2876738ed'}

    iv = bytes.fromhex(out['iv'])
    ct = bytes.fromhex(out['ct'])
    key = sha256(str(g).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.decrypt(ct)
    return ct

N = 13185232652915309492470700885494158416479364343127310426787872363041960044885500175769971795951432028221543122753022991035176378747918784016983155565886369

# https://math.stackexchange.com/questions/1295267/prove-gcdna-1-nb-1-n-gcda-b-1
# gcd(n^a-1, n^b-1) == n^gcd(a, b) - 1

# make a list of primes of 9 bit size
from sympy import sieve
p = list(sieve.primerange(1, 512))

# got damn lucky that there was only one common factor for gcd in the gcd(a, b); so bruteforced through all the possible primes
# and found N^prime - 1 for all the primes and then just ran a checking if condition
for i in p:
    g = N**i - 1
    ct = decrypt(g)
    if b'cr3{' in ct:
        break
        
ct









