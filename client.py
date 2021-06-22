import requests
import os
import base64
import cv2
import json
import numpy as np

## 本地读取图片编码进行传递
with open('C:/Users/LLL/Desktop/20190827162517343.jpg', 'rb') as f:
        # image_bytes = f.read()
        image_bytes = base64.b64encode(f.read())
        image_bytes = image_bytes.decode('ascii')
img = image_bytes

#response = requests.get("http://10.130.14.58:16024/autoExtract/downloadImg", {"projectId": "1001120020200110"})
#img = response.text

projectID = 'projectID_1'
unit_width = 255
unit_height = 255
num_classes = 2
data = {'projectID':projectID, 'img':img, 'unit_width':unit_width,
        'unit_height':unit_height, 'num_classes':num_classes}
resp = requests.post("http://127.0.0.1:8000/stream_predict", data=data)

print(resp.text)
