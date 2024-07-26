from Crypto.Util.number import long_to_bytes,bytes_to_long,GCD  
pt=b"flag{Easy_RSa_1s_e4sy}"
p=16
q=25
n=p*q
e=65537
ct=pow(bytes_to_long(pt),e,n)
print(ct)
print(f"Enc: {ct}")
#ct=125
#n=400
#e=65537
phi=(p-1)*(q-1)
print(f"phi: {phi}")
print(GCD(e,phi))
d=pow(e,-1,phi)
print(f"d: {d}")
pt=pow(ct,d,n)
print(long_to_bytes(pt))