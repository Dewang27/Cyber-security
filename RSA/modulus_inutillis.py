import gmpy2
from Crypto.Util.number import long_to_bytes, inverse, bytes_to_long

e = 3
ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

# Compute the eth root of the ciphertext
root, exact = gmpy2.iroot(ct, e)

# Convert it to bytes
pt = long_to_bytes(int(root))
print(pt.decode('utf-8'))