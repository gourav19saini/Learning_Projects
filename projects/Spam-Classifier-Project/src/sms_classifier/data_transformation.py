import os
import sys
import pandas as pd
import numpy as np

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from src.utils import *

@dataclass
class DataTransformationConfig:
    input_preprocessor_path:str = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()


    def get_data_transformation_object(self):
        try:
            independent_label = ['message']
            dependent = ['label']

            in_pipeline = Pipeline(
                steps=[
                    ("stemmer", Stem()),
                    ("cv", CountVectorizer(max_features=3000)),
                    ("to_array", ToArray())
                ]
            )

            le = LabelEncoder()

            return (
                in_pipeline,
                le
            )
            
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, raw_data_path):
        logging.info('Initiating Data Transformation')
        try:
            logging.info('reading the data as a df')
            data = pd.read_csv(raw_data_path)

            X = data['message']
            y = data['label']

            input_processor, output_processor = self.get_data_transformation_object()
            logging.info('got the data transformation objects')

            X_processed = input_processor.fit_transform(X)
            print(X_processed.shape)
            y_processed = output_processor.fit_transform(y)
            print(y_processed.shape)
            logging.info('Processed the data')

            logging.info('Creating a dataframe from new data')
            data = np.c_[X_processed, y_processed]
            print(data.shape)


            save_object(
                file_path=self.data_transformation_config.input_preprocessor_path,
                obj=input_processor
            )

            return (
                data
            )
            


        except Exception as e:
            raise CustomException(e, sys)