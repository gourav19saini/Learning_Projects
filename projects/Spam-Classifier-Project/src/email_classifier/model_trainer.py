import os
import sys

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    model_path:str = os.path.join('artifacts', 'email_model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, final_data):
        logging.info('Initiating model trainer')
        try:
            logging.info('Separating data into dependent and independent data')
            X = final_data[:, :-1]
            y = final_data[:, -1]
            print(f"shape of X = {X.shape}")
            print(f"shape of y = {y.shape}")

            logging.info('Initiating train test split')
            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25)
            print(f"shape of X_train is {X_train.shape}")
            print(f"shape of X_test is {X_test.shape}")
            print(f"shape of y_train is {y_train.shape}")
            print(f"shape of y_test is {y_test.shape}")

            model = MultinomialNB()
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)
            f1 = f1_score(y_test, y_test_pred)

            if(f1 > 0.6):
                save_object (
                    file_path=self.model_trainer_config.model_path,
                    obj=model
                )

            return f1
        except Exception as e:
            raise CustomException(e, sys)