import binascii
from Crypto.Util.number import long_to_bytes,bytes_to_long

ct = "0f01d27bfc4c93f023cffdf8cd8f43b0a574b7ba70484ff3b36d65d41a01397dc684da97a7b5be14bb56671b9edaaff9e57bfdf747e092d408962dcb9452b9667f9bb2a7e398cf2493e62e6f471ec675756b257245b21fabe646f1271acb5833161f584ac3fc3d71e255110ee2e57c2eb865"
ct = binascii.unhexlify(ct)
ct = bytes_to_long(ct)

from Crypto.PublicKey import RSA

def extract_private_key_from_pem(pem_file_path):
    with open(pem_file_path, 'r') as file:
        private_key = RSA.import_key(file.read())
    print("n=",private_key.n)  
    print("e=",private_key.e)  


extract_private_key_from_pem("C:\\Users\\DewangC\\Downloads\\lmaolmao.pem")
import gmpy2
e=3
n= 87735778682248584456733296719049172409699989786415291411708614353073812040038547567906213789987316756698443576762741968064911827627330301038207597259615790202214922852593846721931899881090246833043568932973315396946666468726585997486096974824031502337015789733572974992310349422109714698083128053071905024439
root, exact = gmpy2.iroot(ct, e)

# Convert it to bytes
pt = long_to_bytes(int(root))
print(pt.decode('utf-8'))












