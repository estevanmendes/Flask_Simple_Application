import pandas as pd
class Dataset:
    
    datasets=[]

    @classmethod
    def add_object(cls,name):
        cls.datasets.append(name)

    @classmethod
    def get_obtjects(cls):
        return cls.datasets



    def __init__(self,name,max_rows,dtypes)-> None:
        self.name=name
        self.max_rows=max_rows
        self.schema=dtypes
        Dataset.add_object(name=name)
    
    def _create_dataframe(self)->pd.DataFrame:

        dataframe={}
        return dataframe