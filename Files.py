import datetime
import os

class Files:

    @staticmethod
    def create_file(path:str) -> str:
        data=str(datetime.datetime.now())
        with open(path,'w') as f:
            f.write(data)

        return data
    
    @staticmethod
    def erase_file(path:str) -> None:
        os.remove(path)

    @staticmethod
    def check_filename_in(list_of_files:list,filename:str) -> bool:
        if filename in list_of_files:
            return True
        else:
            return False    
    
    def error_messages(type):
        """
        Decorator for returning proper error messages
        type:["overwriting","nonexistent"]
        """
        def _message(method):
            def wrapper(self,*args,**kwargs):
                if kwargs.get('filename'):
                    filename=kwargs['filename']
                else:
                    filename=args[0]      

                filenameIn=Files.check_filename_in(self.names,filename)                
                if type=="overwriting" and filenameIn:                                     
                    return'The filename already exist, please delete it before creating a new'   
                             
                elif type=='nonexistent' and not filenameIn:
                    return 'The filename does not exist, please create it before.'   
                             
                else:
                    return method(self,*args,**kwargs)
                
            return wrapper         
        return _message

    def __init__(self,root_path:str,extension:str='.txt') -> None:
        """
        root_path: Path in which all files will be created
        """
        self.root_path=root_path
        self.extension=extension
        self.names=[]
        self.paths={}


    @error_messages('overwriting')
    def add_file(self,filename:str) -> str:      
        self.names.append(filename)
        path=self.get_path(filename)
        self.paths[filename]=path
        return Files.create_file(path)

    @error_messages('nonexistent')
    def remove_file(self,filename:str) -> str:
        Files.erase_file(self.paths[filename])
        self.names.remove(filename)
        del self.paths[filename]
        return f'{filename} deleted'
    
    @error_messages('nonexistent')
    def load_file(self,filename) -> str:
        with open(self.paths[filename],'r') as f:
            data=f.read()
        return data
    
    @error_messages('nonexistent')
    def edit(self,filename:str) -> str:
        Files.erase_file(self.paths[filename])
        return Files.create_file(self.paths[filename])

    def get_path(self,filename:str) -> str:
        return os.path.join(self.root_path,filename+self.extension)  

    def __str__(self) -> str:
        return f"{len(self.names)} Files with extension {self.extension}"


if __name__=="__main__":
    ExampleFiles=Files(root_path='sample_folder',extension='.txt')
    print(ExampleFiles.add_file(filename='someFile'))
    print(ExampleFiles.edit(filename='someFile'))
    print(ExampleFiles.remove_file(filename='someFile'))
    print(ExampleFiles.remove_file(filename='someFile'))
