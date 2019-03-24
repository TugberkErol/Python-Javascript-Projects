from flask import Flask, render_template, request,send_from_directory,redirect
from werkzeug import secure_filename
import text2
import base64
from types import *
import image
import wordEncryption as word
import os
from flask_cors import CORS, cross_origin
from json import *
from flask import jsonify
app = Flask(__name__, static_folder='../static/dist', template_folder='../static')
CORS(app)
server_path=os.getcwd()
@app.route('/')
def upload_file():
   #return render_template('upload.html')
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
	if request.method == 'POST':
		f=request.files['file']
		
		filename=f.filename
		length=len(filename)
		#script_dir = os.path.dirname(__file__)
		rel_path ="/home/ubuntu/uploadfiles/"
		#abs_file_path = os.path.join(script_dir, rel_path)

		if '.txt' in filename:
			text = request.form['text']
			text2.encrypt(filename,text,rel_path)
	
		if '.docx' in filename:
			text = request.form['text']	
			word.encrypt_file(filename,text,rel_path)
	
		if '.jpg' in filename:
			text = request.form['text']
			image.encrypt(filename,text,rel_path)
	#os.chdir("/home/ubuntu/Desktop/uploadfiles/")
	return 'Encrypted'

@app.route('/download_File' ,methods=['GET','POST'])
def download_File():
	os.chdir(server_path+"/encrypted_files")
	if request.method == 'POST':
		textKey = request.form['text']
		fileName=request.form['text2']
		if '.txt' in fileName:
			text2.decrypt(fileName,textKey)
	if request.method == 'POST':
		textKey = request.form['text']
		fileName=request.form['text2']
		if '.jpeg' in fileName:
			image.decrypt(fileName,textKey)
	if request.method == 'POST':
		textKey = request.form['text']
		fileName=request.form['text2']
		if '.docx' in fileName:
			word.decrypt_file(fileName,textKey)
	os.chdir(server_path)
	return 'Downloaded!!!'
@app.route('/list_files',methods=['GET','POST'])
def list_files():
	path=server_path+"/encrypted_files"
	file=os.listdir(path)
	files='---'.join(file)
	return files
@app.route('/deletee',methods=['GET','POST'])
def deletee():
	path=server_path+"/encrypted_files"
	os.chdir(path)
	file=request.form['text']
	os.remove(file)
	
if __name__ == '__main__':

   app.run(debug = True,port=5000),
   