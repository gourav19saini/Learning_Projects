import os
import sys
import pandas as pd
import numpy as np

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from src.utils import Stem, ToArray, save_object

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

@dataclass
class DataTransformationConfig:
    processor_path:str = os.path.join('artifacts', 'email_processor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    

    def get_data_transformation_object(self):
        try:
            pipe = Pipeline(
                steps=[
                    ("stemmer", Stem()),
                    ("cv", CountVectorizer(max_features=4000)),
                    ("to array", ToArray())
                ]
            )

            return pipe
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, raw_data_path):
        logging.info('Initiating data transformation')
        try:
            logging.info('reading the data from csv')
            data = pd.read_csv(raw_data_path)

            X = data['text']
            y = data['label']

            input_processor = self.get_data_transformation_object()
            logging.info('Got the data transformation object')

            X_processed = input_processor.fit_transform(X)
            print(X_processed.shape)

            logging.info('Creating a final dataframe after processing')
            data = np.c_[X_processed, np.array(y)]
            print(data.shape)

            logging.info('Saving object')
            save_object (
                file_path=self.data_transformation_config.processor_path,
                obj=input_processor
            )

            return data
        except Exception as e:
            raise CustomException(e, sys)