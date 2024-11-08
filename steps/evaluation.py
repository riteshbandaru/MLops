import logging

from zenml import step
import pandas as pd

@step
def evaluation1(df:pd.DataFrame) -> None:
    pass