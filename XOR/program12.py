import binascii
hex_string="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byte_string=binascii.unhexlify(hex_string)
print(byte_string)


def xor_with_single_byte_key(byte_string, key):
    return bytes([b ^ key for b in byte_string])

def find_key(byte_string):
    for key in range(256):  
        result = xor_with_single_byte_key(byte_string, key)
        if all(32 <= b < 127 or b in (9, 10, 13) for b in result):
            print(f"Key: {key}, Result: {result.decode('ascii')}")

find_key(byte_string)