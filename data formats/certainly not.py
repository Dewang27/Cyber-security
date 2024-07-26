# openssl x509 -inform der -in blah.der -out blah.pem to convert .der into .pem

from Crypto.PublicKey import RSA

def extract_private_key_from_pem(pem_file_path):
    with open(pem_file_path, 'r') as file:
        private_key = RSA.import_key(file.read())

    print("n=",private_key.n)  # n is the modulus


extract_private_key_from_pem("C:\\Users\\DewangC\\Downloads\\blah.pem")

