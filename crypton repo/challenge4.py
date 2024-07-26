from Crypto.PublicKey import RSA
import math 

def extract_private_key_from_pem(pem_file_path):
    with open(pem_file_path, 'r') as file:
        private_key = RSA.import_key(file.read())
    print("n=",private_key.n)  
    print("e=",private_key.e)  

extract_private_key_from_pem("C:\\Users\\DewangC\\Downloads\\lmaolmaolmao.pem")

n= 87735778682248584456733296719049172409699989786415291411708614353073812040038547567906213789987316756698443576762741968064911827627330301038207597259615790202214922852593846721931899881090246833043568932973315396946666468726585997486096974824031502337015789733572974992310349422109714698083128053071905024439
e= 65537

g= math.sqrt(n)
print(g)
f= round(g)
print(f)


