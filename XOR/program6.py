import base64
import string
def edit_dist(buf1, buf2):
    bin1 = binary_digits(buf1)
    bin2 = binary_digits(buf2)
    
    dist = 0
    for b1, b2 in zip(bin1, bin2):
        if b1 != b2:
            dist += 1
    
    return dist

def binary_digits(buf):
    return ''.join('{0:08b}'.format(c) for c in buf)
print(edit_dist("this is a test".encode(), "wokka wokka!!!".encode()))   



# Open the file and read the contents
with open('6.txt', 'r') as f:
    base64_text = f.read()

# Decode the base64 text
decoded_text = base64.b64decode(base64_text)

print(len(decoded_text))

def keysize_edit_distance(ciphertext, keysize):
    prev = None
    diff = 0
    n = 0
    for i in range(0, len(decoded_text), keysize):
        chunk = decoded_text[i:i+keysize]
        if prev:
            diff += edit_dist(chunk, prev) / keysize
            n += 1
        prev = chunk
    diff /= n
    return diff

keysize = min(range(2, 40), key=lambda x: keysize_edit_distance(decoded_text, x))
print(keysize)
#keysize = 29
key = []

blocks = [decoded_text[i:i+keysize] for i in range(0, len(decoded_text), keysize)]

def english_score(data):    
    s = 0
    data = data.lower()
    common = b"etaoin shrdlu"[::-1]
    
    for c in data:
        if chr(c) not in string.printable:
            return 0
        
        i = common.find(c)
        if i != -1:
            s += i
    
    return s
def single_xor(ciphertext, key):
    plain = [x ^ key for x in ciphertext]
    return bytes(plain)

for key_i in range(keysize):
    chunk = b""
    for bl in blocks:
        if key_i < len(bl):
            chunk += bytes([bl[key_i]])

    k = max(range(255), key=lambda x: english_score(single_xor(chunk, x)))
    key.append(k)

bytes(key).decode('ascii')
def repeating_xor(data, key):
    res = []
    for i, c in enumerate(data):
        k = key[i % len(key)]
        res.append(c ^ k)
    return bytes(res)

plaintext = repeating_xor(decoded_text, bytes(key)).decode('ascii')

print(plaintext[:150])

