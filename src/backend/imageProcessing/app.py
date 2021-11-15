from PIL import Image
from flask import Flask, request
from flask_cors import CORS
from io import BytesIO
import base64
import re
from image import *
import timeit
from mimetypes import guess_extension, guess_type

# PROGRAM API

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST'])
def index():
    data = request.get_json()
    start = timeit.default_timer()
    image_data = re.sub('^data:image/.+;base64,', '', data['data'])
    ext = guess_extension(guess_type(str(data['data']))[0])
    if (ext == ".jpg"):
        # ekstensi file jpg
        compressed_image_array = compressThree(BytesIO(base64.b64decode(image_data)), data['percent'])
        compressed_img = Image.fromarray(compressed_image_array)
        buffered = BytesIO()
        compressed_img.save(buffered, format = "JPEG")
    elif (ext == ".png"):
        # ekstensi file png
        compressed_image_array = compressFour(BytesIO(base64.b64decode(image_data)), data['percent'])
        compressed_img = Image.fromarray(compressed_image_array)
        buffered = BytesIO()
        compressed_img.save(buffered, format = "PNG")
    img_byte = buffered.getvalue()
    compressed_string = base64.b64encode(img_byte)
    stop = timeit.default_timer()
    return {"Response": str(compressed_string), "time": stop - start, "ext": ext}


if __name__ == "__main__":
    app.run(debug=True)