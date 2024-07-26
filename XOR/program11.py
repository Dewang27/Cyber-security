#KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
#KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
#KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
#FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
import binascii

keyone= "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
keytwoxorkeyone = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
keytwoxorkeythree= "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
xoredflag="04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


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

#output=binascii.unhexlify(flag)
#print(output)

