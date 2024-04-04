import logging

import joblib
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


class SimpleModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self):
        # Generating synthetic data for demonstration purposes
        X, y = make_regression(n_samples=100, n_features=1, noise=0.4)
        self.model.fit(X, y)
        # Log the training event
        logging.info("Model trained with synthetic data.")
        joblib.dump(self.model, 'model.joblib')
        # Model saved to disk
        logging.info("Model saved after training")

