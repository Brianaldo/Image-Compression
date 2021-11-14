from PIL import Image
from flask import Flask, request
from flask_cors import CORS
import sys
import os
from io import BytesIO
import base64
import re
from image import *
# sys.path.insert(0, os.path.join(os.path.dirname(os.getcwd()), "DataCollecting"))


app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    data = request.get_json()
    image_data = re.sub('^data:image/.+;base64,', '', data)
    compressed_image_array = compress(BytesIO(base64.b64decode(image_data)), 50)
    compressed_img = Image.fromarray(compressed_image_array)
    buffered = BytesIO()
    compressed_img.save(buffered, format = "JPEG")
    img_byte = buffered.getvalue()
    compressed_string = base64.b64encode(img_byte)
    return {"Response": compressed_string}


if __name__ == "__main__":
    app.run(debug=True)