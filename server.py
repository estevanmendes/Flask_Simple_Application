from flask import Flask,request
import os
import datetime





class Files:

    @staticmethod
    def create_file(path):
        data=datetime.datetime.now()
        with open(path,'w') as f:
            f.write(data)

        return data
    
    @staticmethod
    def erase_file(path):
        os.remove(path)
     
    @classmethod
    def check_filename_in(cls,filename):
        if filename in cls.names_list:
            return True
        else:
            return False

    @classmethod
    def get_path(cls,filename):
        return os.path.join(cls.root_path,filename+cls.extension)

    def __init__(self,root_path,extension='.txt') -> None:
        """
        root_path: Path in which all files will be created
        """
        self.root_path=root_path
        self.extension=extension
        self.names=[]
        self.paths={}
  

    def add_file(self,filename):
        if Files.check_filename_in(filename):
            raise ValueError('The filename already exist, please delete it before creating a new')
        
        self.names.append(filename)
        path=Files.get_path(filename)
        self.paths[filename]=path
        return Files.create_file(path)


    def remove_file(self,filename):
        if not Files.check_filename_in(filename):
            raise ValueError('The filename does not exist, please create it before.')
        
        Files.erase_file(self.paths[filename])
        self.names.remove(filename)
        del self.paths[filename]
    
    def load_file(self,filename):
        with open(self.paths[filename],'r') as f:
            data=f.read()
        return data

    def edit(self,filename,line_2_change=None):
        Files.erase_file(self.paths[filename])
        return Files.create_file(path)


    

        
ExampleFiles=Files(root_path='sample_folder',extension='.txt')



app = Flask(__name__)

app.route('/file_handle/<filename>',methods=['GET','POST','PUT','DELETE'])
def file_handler(filename):
    """it creates, edits, delete and delivery files"""
    
    if request.method=="GET":
        data=ExampleFiles.load_file(filename=filename)
        return data
        
    elif request.method=="POST":
        ExampleFiles.add_file(filename=filename)

    elif request.method=="PUT":
        ExampleFiles.edit(filename)
        
    elif request.method=="DELETE":
        ExampleFiles.remove_file(filename=filename)

        