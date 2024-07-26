import binascii

def xor_decrypt(byte_string, key):
    return ''.join(chr(b ^ key) for b in byte_string)

# Open the file and read the contents
with open('4.txt', 'r') as f:
    lines = f.readlines()

# Try all possible keys on each line
for line in lines:
    byte_string = binascii.unhexlify(line.strip())
    for key in range(256):
        result = xor_decrypt(byte_string, key)
        if all(32 <= ord(c) < 127 or c == '\n' for c in result):
            print(f"Line: {line.strip()}, Key: {key}, Result: {result}")

#Now that the party is jumping
            