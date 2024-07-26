import binascii
a=binascii.unhexlify("2652b7ae08b281594c488cf2e6daee43")
b=binascii.unhexlify("d697937950b3090d56828170609a3b23f836e3cc0ed631cb9ce08c4b9785f5f3db5dee5f44adaad3630303062b61d5fa")

def bxor(a, b):
    
    return bytes([ x^y for (x,y) in zip(a, b)])
c=bxor(a,b)

# The output is:b"the kid don't play"
d=binascii.hexlify(c).decode()
print(c)

# The output is:746865206b696420646f6e277420706c6179