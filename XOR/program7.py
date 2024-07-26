import binascii
def xor(message,key):
    return bytes([message[i] ^ key[i%len(key)] for i in range(len(message))])

flag="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

flag=binascii.unhexlify(flag)    
print(flag)
something=xor(flag,'crypto{'.encode())

print(something)

# assuming key as myXORkey cause that makes sense

key="myXORkey"

output=xor(flag,key.encode())   

print(output)

