from flask import Flask,request
import os
import datetime
from Files import Files
import random
import pandas as pd


ExampleFiles=Files(root_path='sample_folder',extension='.txt')
if not os.path.exists('sample_folder'):
    os.mkdir('sample_folder')
print(ExampleFiles)

app = Flask(__name__)

@app.get('/')
def default():
    print('something')
    return "Welcome to the server to send command related to file management use the endpoint  /file_handler/<filename>"

@app.route('/file_handler/simple_example/<string:filename>',methods=['GET','POST','PUT','DELETE'])
def simple_example(filename):
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
    

def error():
    pass
    
def create_dataset(dataset_info):

    default_path='datasets'
    if not os.path.exists('datasets'):
        os.mkdir('datasets')
    deafult_extension='csv'
    default_max_rows=1000

    if dataset_info.get('schema'):
        schema=dataset_info.get('schema')
        if schema.get('columns'):
            columns=schema.get('columns')
        else:
            error()
        
        if schema.get('max_rows'):
            max_rows=schema.get('max_rows')
        else:
            max_rows=default_max_rows

    if dataset_info.get('extension'):
        extension=dataset_info.get('extension')
    else:
        extension=deafult_extension

    if dataset_info.get('datasetName'):
        datasetName=dataset_info.get('datasetName')
    else:
        dataset_name='Unkown_'+str(random.randint(1,1000))+str(random.randint(1,1000))
    
    os.path.join(default_path,datasetName)
    dtypes={}
    
    _create_pandas_dataframe(columns,dtypes,max_rows)

def    _create_pandas_dataframe(path,columns,dtypes,max_rows):
    pd.DataFrame(columns=columns,dtypes=dtypes).to_csv()






    




@app.route('/file_handler/dataset/<string:datasetId>/config',methods=['GET','POST'])
def dataset(datasetId):
    if request.is_json:
        body=request.json
        print(body)
  

    if request.method=="GET":
        return {'dataset':'yes'}
    
    
    elif request.method=="POST":
        create_dataset(body)        
        return {'created':'yes'}




@app.route('/file_handler/dataset/<string:extension>')
def dataset_edit(extension):

    if request.method=="GET":
        pass
    elif request.method=="POST":
        create_dataset()

        pass
    elif request.method=="PUT":
        pass

    elif request.method=="DELETE":
        pass


if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)