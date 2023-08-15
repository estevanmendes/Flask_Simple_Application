import pandas as pd
import os

class Dataset:
    
    default_path='datasets'
    datasets=[]

    @classmethod
    def created_root_dir(cls):
        if not os.path.isdir(cls.default_path):
            os.mkdir(cls.default_path)

    @classmethod
    def add_object(cls,name):
        cls.datasets.append(name)

    @classmethod
    def get_obtjects(cls):
        return cls.datasets

    def create_path(root_path,dataset_name)-> str:
        return os.path.join(root_path,dataset_name)
    
    @staticmethod
    def save_dataframe(df:pd.DataFrame,path:str,extension:str):
        if extension=="csv":
            df.to_csv(path,index=False,sep=',')

    def add_extension(name,extension):
        return name+'.'+extension

    def __init__(self,name,max_rows,columns,dtypes,extension)-> None:
        self.name=name
        self.max_rows=max_rows
        self.columns=columns
        self.schema=dtypes
        self.extension=extension
        self.filename=Dataset.add_extension(name,extension)
        self.path=Dataset.create_path(Dataset.default_path,self.filename)
        Dataset.add_object(name=name)
        Dataset.created_root_dir()
        self._create_dataframe()

    
    def _create_dataframe(self)->pd.DataFrame:
        print(self.schema)
        df=pd.DataFrame(columns=self.columns)
        df=df.astype(self.schema)
        self.df=df
        self.save()
        return df

        
    def save(self):
        Dataset.save_dataframe(self.df,self.path,self.extension)
    
    def __str__(self) -> str:
        return f"datasetName:{self.name},max_rows:{self.max_rows},extension:{self.extension},columns:{self.columns}"
    

if __name__=='__main__':
    Dataset('test',10,['t1'],{'t1':'int'},'csv')