# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from PIL import Image
import base64
import numpy as np
import os
import cv2



Image.MAX_IMAGE_PIXELS = None

app = Flask(__name__)

@app.route('/stream_predict', methods=['POST'])
def img_infer():
    if request.method == 'POST':
       projectID = request.form.get('projectID')
       img = request.form.get('img')
       unit_width = request.form.get('unit_width')
       unit_height = request.form.get('unit_height')
       num_classes = request.form.get('num_classes')

       img = base64.b64decode(img.encode('ascii'))
       image_data = np.frombuffer(img, np.uint8)
       image_data = cv2.imdecode(image_data, cv2.IMREAD_GRAYSCALE)
       ori_img_array = image_data
       print(type(ori_img_array))
       print('img_shape: ', ori_img_array.shape)




       print(projectID)
       print(unit_height,unit_width) 



    return 'done'

if __name__ == "__main__":
    # app.run(host="172.23.132.130", port=5005)
    # app.run(host="0.0.0.0", port=5005)
    app.run(host="127.0.0.1", port=8000)
