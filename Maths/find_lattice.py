from Crypto.Util.number import getPrime, inverse, bytes_to_long
import random
import math

q=7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
h=2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
e=5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

upper_bound = 61798997242895964372941272076217635561377665933371777951776437204406832726016
lower_bound = 43698490020980491271854387304594103105874493088655744395288203235085122535424

print(len(str(upper_bound)))

def recover_m(q, h, e):
    # Calculate g/f
    gf = (h * inverse(e, q)) % q

    # Calculate the nearest multiple of g/f to e
    m = round(e / gf) * gf

    return m

# Recover the original message m
recovered_m = recover_m(q, h, e)

# Convert the long integer back to bytes
from Crypto.Util.number import long_to_bytes
recovered_flag = long_to_bytes(recovered_m)

print(f'Recovered Flag: {recovered_flag}')