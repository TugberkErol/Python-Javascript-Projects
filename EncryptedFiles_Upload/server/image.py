import os
from PIL import Image 
import math
from Crypto.Cipher import AES
import hashlib
import hashlib
server=os.getcwd()
download_path="/home/ubuntu/download"

def encrypt(imagename,password,path):
    password = hashlib.sha256(password.encode("utf-8")).digest()
    plaintext = list()
    plaintextstr = ""
    server_path=os.getcwd()+"/encrypted_files"
    os.chdir(path)
   
    im = Image.open(imagename) 
    pix = im.load()
    
  
    width = im.size[0]
    height = im.size[1]
    
    
    for y in range(0,height):    
        for x in range(0,width):
            #print pix[x,y]
            plaintext.append(pix[x,y])
            

    for i in range(0,len(plaintext)):
        for j in range(0,3):
            plaintextstr = plaintextstr + "%d" %(int(plaintext[i][j])+100)
    
    relength = len(plaintext)
    
   
    plaintextstr += "h" + str(height) + "h" + "w" + str(width) + "w"
    
    while (len(plaintextstr) % 16 != 0):
        plaintextstr = plaintextstr + 'n'

    obj = AES.new(password, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(plaintextstr)
   
    cipher_name ="ilkresim.jpeg"
    os.chdir(server_path)
    g = open(cipher_name, 'wb')
    g.write(ciphertext)
    os.chdir(server),
    #for tr in range(0,100):
     #   print "plaintext ",ciphertext[tr]
        
   
  
    #encr=Image.new("RGB",(int(width),int(height)))
   # encr.putdata(f)    

def decrypt(ciphername,password):
    password = hashlib.sha256(password.encode("utf-8")).digest()
    cipher=open(ciphername,'rb')
    ciphertext=cipher.read()

    obj2=AES.new(password,AES.MODE_CBC,'This is an IV456')
    decrypted=obj2.decrypt(ciphertext)
    #print(decrypted)   
    decrypted =decrypted.replace("n","")
    #print(decrypted)
    newwidth=decrypted.split("w")[1]
    newheight=decrypted.split("h")[1]
    #print(decrypted)
    
    heightr = "h" + str(newheight) + "h"
    widthr = "w" + str(newwidth) + "w"
    print("heightr "+heightr+"widthr "+widthr)
    decrypted = decrypted.replace(heightr,"")
    decrypted = decrypted.replace(widthr,"")
    a=len(decrypted)
    print(a)
    step = 3
    finaltextone=[decrypted[i:i+step] for i in range(0, len(decrypted), step)]
    #print("decrypted "+len(decrypted))
    finaltexttwo=[(int(finaltextone[int(i)])-100,int(finaltextone[int(i+1)])-100,int(finaltextone[int(i+2)])-100) for i in range(0, len(finaltextone), step)]    
    b=len(finaltextone)
    print(b)
    # reconstruct image from list of pixel RGB tuples
    os.chdir(download_path)
    newim = Image.new("RGB", (int(newwidth), int(newheight)))
    newim.putdata(finaltexttwo)
            
    #newim.show()
    newim.save("decryptedimage","jpeg")
