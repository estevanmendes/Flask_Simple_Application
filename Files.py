import datetime
import os

class Files:

    @staticmethod
    def create_file(path):
        data=str(datetime.datetime.now())
        with open(path,'w') as f:
            f.write(data)

        return data
    
    @staticmethod
    def erase_file(path):
        os.remove(path)
     


    def __init__(self,root_path,extension='.txt') -> None:
        """
        root_path: Path in which all files will be created
        """
        self.root_path=root_path
        self.extension=extension
        self.names=[]
        self.paths={}

    def check_filename_in(self,filename):
        if filename in self.names:
            return True
        else:
            return False

    def get_path(self,filename):
        return os.path.join(self.root_path,filename+self.extension)  

    def add_file(self,filename):
        if self.check_filename_in(filename):
            return'The filename already exist, please delete it before creating a new'
          
        self.names.append(filename)
        path=self.get_path(filename)
        self.paths[filename]=path
        return Files.create_file(path)


    def remove_file(self,filename):
        if not self.check_filename_in(filename):
            return 'The filename does not exist, please create it before.'
        
        Files.erase_file(self.paths[filename])
        self.names.remove(filename)
        del self.paths[filename]
        return '{filename} deleted'
    
    def load_file(self,filename):
        if not self.check_filename_in(filename):
            return 'The filename does not exist, please create it before.'
        
        with open(self.paths[filename],'r') as f:
            data=f.read()
        return data

    def edit(self,filename,):
        if not self.check_filename_in(filename):
            return 'The filename does not exist, please create it before.'
        Files.erase_file(self.paths[filename])
        return Files.create_file(self.paths[filename])

    def __str__(self) -> str:
        return f"{len(self.names)} Files with extension {self.extension}"