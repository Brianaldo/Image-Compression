from PIL import Image
from flask import Flask, request
from flask_cors import CORS
import sys
import os
from io import BytesIO, StringIO
import base64
import re
from image import *
# sys.path.insert(0, os.path.join(os.path.dirname(os.getcwd()), "DataCollecting"))


app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    # print(request.get_json())
    data = request.get_json()
    image_data = re.sub('^data:image/.+;base64,', '', data)
    compressed_image_array = compress(BytesIO(base64.b64decode(image_data)), 50)
    compressed_string = base64.encode(Image.fromarray(compressed_image_array))
    # im.save("coba.jpg")
    print(compressed_string)
    # image = Image.open(StringIO.StringIO(image_data))
    return {"Response": "hello"}


if __name__ == "__main__":
    app.run(debug=True)