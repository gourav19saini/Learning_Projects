import os
import sys
import numpy as np
import pandas as pd


from src.exception import CustomException
from src.utils import load_object

class SMSPredictPipeline:
    def __init__(self):
        pass

    def predict(self, ser):
        try:
            model_path = os.path.join('artifacts', 'model.pkl')
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            print('Before Loading')
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)

            print("after loading")
            data_scaled = preprocessor.transform(ser)
            print(f"shape of data after processing is {data_scaled.shape}")

            print(data_scaled)

            pred = model.predict(data_scaled)
            return pred

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, text):
        self.text = text
    
    def get_data_as_series(self):
        try:
            print(self.text)
            data = np.array([self.text])
            ser = pd.Series(data, index=[0])
            return ser
        except Exception as e:
            raise CustomException(e, sys)


class EmailPredictPipeline:
    def __init__(self):
        pass

    def predict(self, ser):
        try:
            model_path = os.path.join('artifacts', 'email_model.pkl')
            preprocessor_path = os.path.join('artifacts', 'email_processor.pkl')

            print('before loading')
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)

            print("after loading")
            data_scaled = preprocessor.transform(ser)
            print(f"shape of data after processing is {data_scaled.shape}")

            print(data_scaled)

            pred = model.predict(data_scaled)
            return pred

        except Exception as e:
            raise CustomException(e, sys)