import logging
from zenml import step
from src.data_cleaning import Data_cleaning,Data_preprocessing,Data_divide
import pandas as pd
from typing import Annotated
from typing import Tuple

@step
def clean_data1(df:pd.DataFrame) ->Tuple[Annotated[pd.DataFrame,"X_train"],Annotated[pd.DataFrame,"X_test"],Annotated[pd.Series,"Y_train"],Annotated[pd.Series,"Y_test"]]:
    try:
        process=Data_preprocessing()
        d1=Data_cleaning(df,process)
        processed_data=d1.clean_data()

        divide=Data_divide()
        data_cleaning=Data_cleaning(processed_data,divide)
        X_train,X_test,Y_train,Y_test=data_cleaning.clean_data()
        logging.info(f"Successfully cleaned the data")
    except Exception as e:
        logging.error(f"Error occured while cleaning the data: {e}")
        raise e
