from Crypto.Util.number import long_to_bytes,bytes_to_long

import binascii

ct = "57f1475ae4d803f0536cb62b0111cfcde087ae804fda2e1cf6498c367ee3a1d75d926cedd9d9883f189c3d9f0836bf1a636fcae407a103bde88e39095ec90abc13287432d0271ad2c7e937c191bf049cee3d69b3c280c5e9e25900be0917caa30b51d0fe049c11702f341f7106cb00fcc9e93abd980f09d6d9ae259868e72bfa"
ct = binascii.unhexlify(ct)

ct = bytes_to_long(ct)

p = 6958271393287170117448891021448827870244652620796166337874899406278127643022124226656230972235829204217718701711355755622520840943962368410353060326959627
q = 10816988558466468069802205154113557859050665172995721741674476865844313409030354507360669179381457836401919224815040955096510785560864262908230559354811907
n= p*q
phi=(p-1)*(q-1)
d=pow(65537,-1,phi)
m=pow(ct, d,n)
print(long_to_bytes(m))