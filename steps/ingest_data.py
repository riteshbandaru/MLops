import logging
import pandas as pd
from zenml import step

class Ingestdata():

    def __init__(self,data_path:str):
        self.data_path=data_path

    
    def get_data(self):
        logging.info(f"Ingesting data from{self.data_path}")

        return pd.read_csv(self.data_path)
    

@step
def Ingest_data(data_path:str) -> pd.DataFrame:
    """
    1)Ingest data
    2)Args
    3)Return the data
    """
    try:
        data=Ingestdata(data_path)
        df=data.get_data()
        return df
    except Exception as e:
        logging.error(f"Ingestion error{e}")

        raise e


