import pandas as pd
import os
from typing import Union
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
    def save_dataframe(df:pd.DataFrame,path:str,extension:str)-> None:
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
        self._df=df
        self.save()
        return df

        
    def save(self)->None:
        Dataset.save_dataframe(self._df,self.path,self.extension)
    
    def __str__(self) -> str:
        return f"datasetName:{self.name},max_rows:{self.max_rows},extension:{self.extension},columns:{self.columns}"
    
    @property
    def df(self)->str:
        return self._df.to_string()

    def get_df(self,start_row:Union[int,None]=None,end_row:Union[int,None]=None)->str:
        if not start_row:
            start_row=0
        if not end_row:
            end_row=-1

        return self._df.iloc[start_row:end_row].to_string()

    def add_rows(self,data:dict,start_row:Union[int,None]=None)->int:
        df_increment=pd.DataFrame(data)
        if start_row:
            df=pd.concat([self._df.iloc[:start_row],df_increment],axis=0)
            self._df=pd.concat([df,self._df.iloc[start_row:]],axis=0)
            del df
        else:
            self._df=pd.concat([self._df,df_increment],axis=0)
        self.save()
        incremented_rows=len(df_increment)
        del df_increment
        return incremented_rows

    def delete_rows(self):
        pass

        

if __name__=='__main__':
    d1=Dataset('test',10,['t1'],{'t1':'int'},'csv')
    d1._df=pd.DataFrame({'t1':[1,2,3],'t2':['ab','bc','cd']})
    
    print(d1.get_df(None,None))
    print(type(d1._df))