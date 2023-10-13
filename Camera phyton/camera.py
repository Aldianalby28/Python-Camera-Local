import requests
import numpy as np
import cv2
while True:
  images = requests.get("192.168.233.78:8080/shot.jpg")
  video=np.array(bytearray(video.content),dtype= np.uint8)
  render = cv2.imdecode(video,-1)
  cv2.imshow('frame',render)
  if(cv2.waitkey(1) and 0xFF==ord('q')):
    break
