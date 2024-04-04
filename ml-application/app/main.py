import logging
import os

from flask import Flask, request, jsonify

from .serve import ModelServer
from .train import SimpleModel

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

app = Flask(__name__)


def ensure_model_is_trained():
    model_path = 'model.joblib'
    if not os.path.exists(model_path):
        logging.info("Trained model not found. Training a new model...")
        model_to_train = SimpleModel()
        model_to_train.train()


# In production system, training should be done separately
# model should be loaded from disk or cloud storage or model registry
# we do not want to train model for every prediction request
# but for simplicity, we are training the model here ONLY ONCE for the first time
# after that we will load the model from disk and use it for prediction
ensure_model_is_trained()  # Check if the model is trained and train if necessary


model_server = ModelServer()  # Initialize the model server after ensuring the model is trained


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        feature_value = data['feature_value']
        prediction = model_server.predict(feature_value)
        logging.info(f"Prediction for feature_value {feature_value}: {prediction}")
        return jsonify({'predicted_value': prediction})
    except Exception as e:
        logging.error(f"Error during prediction: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
