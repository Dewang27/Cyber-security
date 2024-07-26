from Crypto.PublicKey import RSA

def extract_private_key_from_pem(pem_file_path):
    with open(pem_file_path, 'r') as file:
        private_key = RSA.import_key(file.read())
    print("d=",private_key.d)  # d is the private exponent
    print("e=",private_key.e)  # e is the public exponent
    print("n=",private_key.n)  # n is the modulus
    print("p=",private_key.p)  # p is the first factor
    print("q=",private_key.q)  # q is the second factor
extract_private_key_from_pem("C:\\DewangData\\VSCode\\Projects\\PYTHON WS\\data formats\\privacyenhancedemail.pem")