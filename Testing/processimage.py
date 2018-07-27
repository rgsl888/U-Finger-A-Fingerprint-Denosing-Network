import glob

images_path = '/home/rgsl888/Finger_Print_dataset/validation_ground-truth/'

img_ext = ".jpg"

#canny_conv_images_path = '/home/rgsl888/Finger_Print_dataset/canny_conv_input/'

gray_conv_images_path = '/home/rgsl888/Finger_Print_dataset/training_ground-truth/'

import os

#if not os.path.exists(canny_conv_images_path):
#    os.makedirs(canny_conv_images_path)
if not os.path.exists(gray_conv_images_path):
    os.makedirs(gray_conv_images_path)

images = glob.glob (images_path + "/*" + img_ext)

print (images[1:10])

import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy

for image in images:
    img = cv2.imread(image,0)
    #edges = cv2.Canny(img,100,200)
    filename = image.split("/")
    #edges = np.where(edges == 255, 0, 255)
    cv2.imwrite (gray_conv_images_path + 'val' + filename[-1], img)
    #cv2.imwrite (canny_conv_images_path + filename[-1], edges)
