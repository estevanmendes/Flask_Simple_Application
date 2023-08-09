from flask import Flask,request
import os
import datetime
from Files import Files

ExampleFiles=Files(root_path='sample_folder',extension='.txt')
print(ExampleFiles)

app = Flask(__name__)

@app.get('/')
def default():
    print('something')
    return "Welcome to the server to send command related to file management use the endpoint  /file_handle/<filename>"

@app.route('/file_handler/<string:filename>',methods=['GET','POST','PUT','DELETE'])
def file_handler(filename):
    """it creates, edits, delete and delivery files"""

    if request.method=="GET":
        data=ExampleFiles.load_file(filename=filename)
        return data  
          
    elif request.method=="POST":
        return ExampleFiles.add_file(filename=filename)

    elif request.method=="PUT":
        return ExampleFiles.edit(filename)

    elif request.method=="DELETE":
        return ExampleFiles.remove_file(filename=filename)

if __name__== '__main__':
    app.run(host='0.0.0.0', port=3000)