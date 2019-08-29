import keyring
import base64
import os
from sys import argv
from keyrings.cryptfile.cryptfile import CryptFileKeyring

def secure_keyring_access(keyring_name=None):
    "Encrypted Keyring file access."
    kr = CryptFileKeyring()
    kr._unlock()
    return(kr)

def secure_keyring_get(name, kr):
    "Gets encrypted Keyring password."
    return(kr.get_password('service',name))

def keyring_get(name, kr=keyring.backends.Windows):
    "Gets standard Keyring password."
    k = keyring.get_credential(kr, name)
    return(k.__dict__[name])

def keyring_set(name, password, kr=keyring.backends.Windows):
    "Sets standard Keyring password."
    keyring.set_password(kr, name, password)

if __name__ == '__main__':
    kr = secure_keyring_access()
    passwd = secure_keyring_get(input("Name of the password you want: "), kr)
    print(passwd)


# from cryptography.fernet import Fernet
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# def create_hash(hashable, derivator, iterations=100000):
#     "Passes the hashable password through a Key Derivation Function which takes a password called derivator to encrypt it."
#     encryption_pass = bytes(derivator, 'utf-8')
#     password = bytes(hashable, 'utf-8')
#     salt = os.urandom(32)
#     kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
#      length=32,
#      salt=salt,
#      iterations=iterations,
#      backend=default_backend())
#     key = base64.urlsafe_b64encode(kdf.derive(encryption_pass))
#     return(salt, Fernet(key).encrypt(password))