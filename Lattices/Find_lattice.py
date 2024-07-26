from Crypto.Util.number import getPrime, inverse, bytes_to_long
import random
import math



q=7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257
h=2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800

e=5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

upper_bound = int(math.sqrt(q // 2))
lower_bound = int(math.sqrt(q // 4))


from Crypto.Util.number import long_to_bytes

def brute_force_decrypt(q, h, e):
    upper_bound = int(math.sqrt(q // 2))
    for f in range(2, upper_bound):
        for g in range(2, upper_bound):
            if math.gcd(f, g) == 1:
                try:
                    a = (f*e) % q
                    m = (a*inverse(f, g)) % g
                    flag = long_to_bytes(m)
                    if flag.startswith(b"crypto{"):
                        return flag
                except:
                    continue
    return None



flag = brute_force_decrypt(q, h, e)
if flag:
    print(f"Decrypted flag: {flag}")
else:
    print("Failed to decrypt flag")
