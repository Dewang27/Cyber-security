import binascii
hex_string="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
byte_string=binascii.unhexlify(hex_string)
print(''.join(chr(b) for b in byte_string))
#or another way is 
hex_strings="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
byte_strings=bytes.fromhex(hex_strings)
print(byte_strings.decode('utf-8'))