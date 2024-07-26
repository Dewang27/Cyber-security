a="label"
b=13

def xor(a,b):
    return ''.join(chr(ord(x)^b) for x in a)
print(xor(a,b))