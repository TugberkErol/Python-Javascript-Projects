from Crypto import Random
from Crypto.Cipher import AES
import base64
import hashlib
import os

BLOCK_SIZE=16
server=os.getcwd()
cipher_name=""
download_path="/home/ubuntu/download"
def encrypt(message, password,path):
	private_key = hashlib.sha256(password.encode("utf-8")).digest()
	server_path=os.getcwd()+"/encrypted_files"
	os.chdir(path)
	im =open(message,"r") 
	message2 =im.read()
   	while (len(message2) % 16 != 0):
   		message2 = message2 + 'n'
	obj = AES.new(private_key, AES.MODE_CBC, 'This is an IV456')
	ciphertext = obj.encrypt(message2)
   	cipher_name ="yenideneme.txt"
   	os.chdir(server_path)
 	g = open(cipher_name, 'wb')
 	g.write(ciphertext)
 	os.chdir(server)
def decrypt(message,password):
	im2=open(message,'r')
	message3=im2.read()
 	private_key = hashlib.sha256(password.encode("utf-8")).digest()
 	cipher=AES.new(private_key,AES.MODE_CBC,'This is an IV456')
 	encrypted_message=cipher.decrypt(message3)
 	encrypted_message=encrypted_message.replace("n","")
 	os.chdir(download_path)

 	g=open("kayit",'wb')
 	g.write(encrypted_message)
 	im2.close()
 	