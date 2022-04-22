from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import hashlib
import glob
from Crypto.PublicKey import RSA
rsa = RSA.generate(2048)
privateK = rsa.exportKey()
publicK =rsa.public_key().exportKey()


with open('private_key.pem','rb') as f :
    privateK = f.read()


with open('encrypted.pem','rb') as f:
    encrypted_key = f.read()

rsa_privkey = RSA.importKey(privateK)
cipher = PKCS1_OAEP.new(rsa_privkey)

key = cipher.decrypt(encrypted_key)

with open('encrypted.pem','wb') as f:
    f.write(encrypted_key)



def padded(entry):
    while len(entry)%16 != 0:
        entry = entry + b'0'
    return entry
#
mode = AES.MODE_CBC


file = glob.glob('*enc')
for f in file:

    openfile = open(f,"rb")
    openfile_read = openfile.read()




    IV = 'This is an IV123'.encode()
    cipher = AES.new(key, mode, IV)
    decrypted_img = cipher.decrypt(openfile_read)

    with open('new'+ f.replace(".jpg.enc","") +'.jpg', 'wb') as e:
        e.write(decrypted_img.rstrip(b'0'))


