import logging
from zenml import pipeline
import pandas as pd
from steps.ingest_data import Ingest_data
from steps.clean_data import clean_data1
from steps.model_train import train_model
from steps.evaluation import evaluation1

@pipeline
def train_pipeline(data_path:str) -> None:
    data=Ingest_data(data_path)
    clean_data1(data)
    train_model(data)
    evaluation1(data)

