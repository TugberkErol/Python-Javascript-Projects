from Crypto import Random
from Crypto.Cipher import AES
import hashlib
import os
server=os.getcwd()
download_path="/home/ubuntu/download"
def pad(s):
    padding_size = AES.block_size - len(s) % AES.block_size
    return s + b"\0" * padding_size, padding_size

def encrypt(message, key, key_size=256):
    message, padding_size = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_bytes = iv + cipher.encrypt(message) + bytes([padding_size])    
    return enc_bytes

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    print(cipher)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:-1])
    padding_size = ciphertext[-1] * (-1)
    #return plaintext[:padding_size]
    return plaintext
def encrypt_file(file_name, key,path):
    key = hashlib.sha256(key.encode("utf-8")).digest()
    server_path=os.getcwd()+"/encrypted_files"
    os.chdir(path)
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
        #print(plaintext)   
    #print(type(plaintext))
    enc = encrypt(plaintext, key)
    #print("enc",enc)
    os.chdir(server_path)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)
    os.chdir(server),
def decrypt_file(file_name, key):
    key = hashlib.sha256(key.encode("utf-8")).digest()
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    os.chdir(download_path)
    with open('processed_' + file_name[:-4], 'wb') as fo:
        fo.write(dec)

"""key = '123'
hash_object = hashlib.md5(key.encode())"""

