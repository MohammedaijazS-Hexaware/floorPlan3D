# Import primary module dependencies
from flask import Flask, jsonify, request
import os
import cv2
import time
import json
import base64

# Import local dependencies
from util import plots

# Assing Flask Settings
app = Flask(__name__)
IMAGE_SAVE_PATH = os.path.join(os.getcwd(), 'uploads')

# Assign PORT for service run
PORT = 3006

# Initialize Routes
@app.route("/health",methods = ['GET'])
def check_server_health():
    output = {
        "status": True
    }
    return jsonify(output), 200

@app.route("/generate",methods = ['POST'])
def floor_plan():
    # Handle inputs
    input_payload = request.get_json()
    base_64_string = input_payload["image_string"]
    imgdata = base64.b64decode(base_64_string)

    # Handle every input as separate file with filename as timestamp (Always unqiue)
    filename = str(int(time.time())) + '.jpg'

    # Save input image to local server path
    with open(os.path.join(IMAGE_SAVE_PATH, filename), 'wb') as f:
        f.write(imgdata)
        
    # Call desired utilties
    result = plots.generate_plots(filename)

    # return result as response
    return jsonify(result), 200

# Initiate main script
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)