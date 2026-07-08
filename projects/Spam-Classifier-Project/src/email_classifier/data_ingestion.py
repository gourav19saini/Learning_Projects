import os
import sys

from src.exception import CustomException
from src.logger import logging

import pandas as pd
from dataclasses import dataclass

from src.email_classifier.data_transformation import DataTransformationConfig
from src.email_classifier.data_transformation import DataTransformation
from src.email_classifier.model_trainer import ModelTrainerConfig
from src.email_classifier.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join('artifacts', 'email_raw_data.csv')


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Initiating Data Ingestion')
        try:
            data = pd.read_csv('data/Email/combined_data_new.csv')
            logging.info('Read the data from the csv file')

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)
            logging.info('Created the directory to save the csv file')

            data.to_csv(self.data_ingestion_config.raw_data_path, header=True, index=False)
            logging.info('Saving the data as csv file')

            return(
                self.data_ingestion_config.raw_data_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    data_ingestion_obj = DataIngestion()
    raw_data_path = data_ingestion_obj.initiate_data_ingestion()

    data_transformation_object = DataTransformation()
    final_data = data_transformation_object.initiate_data_transformation(raw_data_path)

    model_trainer_object = ModelTrainer()
    score = model_trainer_object.initiate_model_trainer(final_data=final_data)
    print(score)