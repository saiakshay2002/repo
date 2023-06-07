import cv2
import numpy as np
import matplotlib.pyplot as plt
img =cv2.imread("/home/iwizards/Desktop/pythonfolder/cv1.PNG",1)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

height=img.shape
width=img.shape[1]
#channels=img.shape[2]
si=img.size
print("height",height)
print("wid",width)
#print("chann",channels)
print("size",si)



