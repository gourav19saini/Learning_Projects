import os
import sys
import pandas as pd


from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from src.sms_classifier.data_transformation import DataTransformationConfig
from src.sms_classifier.data_transformation import DataTransformation
from src.sms_classifier.model_trainer import ModelTrainerConfig
from src.sms_classifier.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    

    def initiate_data_ingestion(self):
        logging.info('Initiating Data Ingestion')
        try:
            data = pd.read_csv('data/SMS/SMSSpamCollection', sep='\t', names=['label', 'message'])
            logging.info("read the csv file as a dataframe")

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
    data_processed = data_transformation_object.initiate_data_transformation(raw_data_path)

    print(f"Shape of processed data is {data_processed.shape}")

    model_trainer_object = ModelTrainer()
    score = model_trainer_object.initiate_model_trainer(raw_data=data_processed)
    print(f"Model score is {score}")