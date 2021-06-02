# -*- coding: utf-8 -*-
"""Extracting image in Google street view api.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aW2a5PY77akEvJXviV98zjKvHh0C0Fh5
"""

pip install google_streetview

import google_streetview.api







import requests
meta_base = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
pic_base = 'https://maps.googleapis.com/maps/api/streetview?'
api_key = 'api_key'
location = 'Jalan Doktor Wahidin Sudirohusodo, Kembangan, Gresik Regency, East Java, Indonesia'
meta_params = {'key' : api_key,
               'location' : location}
pic_params = {
	'size': '600x300', # max 640x640 pixels
	'location': location,
	'key': api_key,

}
meta_response = requests.get(meta_base, params=meta_params)

meta_response.json()

pic_response = requests.get(pic_base, params=pic_params)

for key, value in pic_response.headers.items():
    print(f"{key}: {value}")

with open('test.jpg', 'wb') as file:
    file.write(pic_response.content)
# remember to close the response connection to the API
pic_response.close()

# using matpltolib to display the image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.figure(figsize=(10, 10))
img=mpimg.imread('test.jpg')
imgplot = plt.imshow(img)
plt.show()

def detect(location):
  pic_base = 'https://maps.googleapis.com/maps/api/streetview?'
  pic_params = {
	  'size': '600x300', # max 640x640 pixels
	  'location': location,
	  'key': api_key,

  }
  pic_response = requests.get(pic_base, params=pic_params)
  global number = number + 1
  with open('result' + number + '.jpg', 'wb') as file:
    file.write(pic_response.content)
  # remember to close the response connection to the API
  pic_response.close()
  img=mpimg.imread('result' + number + '.jpg')
  return img