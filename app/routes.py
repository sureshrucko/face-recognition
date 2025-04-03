# app/routes.py

from flask import Blueprint, jsonify, request
from app.services.common_service import get_hello_message, face_liveness_check
from app.services.liveness_service import LivenessDetection
import numpy as np
from PIL import Image

api_blueprint = Blueprint('api', __name__)

liveness_checker = LivenessDetection(checkpoint_path="model/OULU_Protocol_2_model_0_0.onnx")

@api_blueprint.route('/api/hello', methods=['GET'])
def hello():
    response = get_hello_message()
    return jsonify(response);

@api_blueprint.route('/api/liveness-check', methods=['POST'])
def liveness_check():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    image = Image.open(file.stream)
    image = image.convert("RGB")
    image_np = np.array(image)

    score = liveness_checker(image_np)
    result = "Live" if score > 0.5 else "Spoof"

    return jsonify({"result": result, "score": score})