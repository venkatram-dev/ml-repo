import logging

import joblib


class ModelServer:
    def __init__(self, model_path='model.joblib'):
        self.model = joblib.load(model_path)
        logging.info("Model loaded for serving")

    def predict(self, feature_value):
        return self.model.predict([[feature_value]])[0]

