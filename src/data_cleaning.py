import logging
import pandas as pd
from typing import Union
from abc import ABC, abstractmethod

from sklearn.model_selection import train_test_split

class Data_cleaning(ABC):
    @abstractmethod
    def clean_data(self, df: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass

class Data_preprocessing(Data_cleaning):

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:

        try:
            data = data.drop(
                [
                    "order_approved_at",
                    "order_delivered_carrier_date",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date",
                    "order_purchase_timestamp",
                ],
                axis=1,
            )
            data["product_weight_g"].fillna(data["product_weight_g"].median(), inplace=True)
            data["product_length_cm"].fillna(data["product_length_cm"].median(), inplace=True)
            data["product_height_cm"].fillna(data["product_height_cm"].median(), inplace=True)
            data["product_width_cm"].fillna(data["product_width_cm"].median(), inplace=True)
            # write "No review" in review_comment_message column
            data["review_comment_message"].fillna("No review", inplace=True)

            data = data.select_dtypes(include=[np.number])
            cols_to_drop = ["customer_zip_code_prefix", "order_item_id"]
            data = data.drop(cols_to_drop, axis=1)

            return data
        except Exception as e:
            logging.error(f"Error occured while cleaning the data: {e}")

class Data_divide(Data_cleaning):

    def clean_data(self, df: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:

        try:
            X = data.drop("review_score", axis=1)
            y = data["review_score"]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(f"Error occured while dividing the data: {e}")


class DataCleaning:
    def __init__(self, data: pd.DataFrame, strategy: Data_cleaning) -> None:
        self.df = data
        self.strategy = strategy

    def clean_data(self) -> Union[pd.DataFrame, pd.Series]:
        return self.strategy.clean_data(self.df)