
#X1= b3c8d73e3a9b23df7cc1253277a4878ef65bcfe9735f29d84424
#X2^X1= fb3514ac2e94885e9d5ec915821650572d5e0b842e9630f32b1b
#X2^X3= d2656867798e8584ec34ab2d4562b1a9c82b8fcf1feeeddf70e2
#FLAG^X1^X3^X2= 07c1de3e3867c32fe29cbd6957a2695f0e021f4b58c2b03446bb

import binascii

keyone= "b3c8d73e3a9b23df7cc1253277a4878ef65bcfe9735f29d84424"
keytwoxorkeyone = "fb3514ac2e94885e9d5ec915821650572d5e0b842e9630f32b1b"
keytwoxorkeythree= "d2656867798e8584ec34ab2d4562b1a9c82b8fcf1feeeddf70e2"
xoredflag="07c1de3e3867c32fe29cbd6957a2695f0e021f4b58c2b03446bb"


def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])
# to get key 2

keytwo = xor(binascii.unhexlify(keytwoxorkeyone), binascii.unhexlify(keyone)).hex()
# to get key 3
keythree= xor(binascii.unhexlify(keytwoxorkeythree), binascii.unhexlify(keytwo)).hex()

key1xorkeytwoxorkeythree=xor(binascii.unhexlify(keytwoxorkeythree), binascii.unhexlify(keyone)).hex()

#FLAG

flag=xor(binascii.unhexlify(key1xorkeytwoxorkeythree), binascii.unhexlify(xoredflag))
print(flag) 


