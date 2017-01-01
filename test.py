import cv2
import numpy as np
from image import Image, create_image_from_file
from normalizer import Normalizer
img = create_image_from_file('raw_images/1649_1109_0003_Amp5-1_B_20070424_D20_w1_066B88BE-96FA-420D-B631-F6E3CF2E71D9.tif')

if not img is None:

    norm = Normalizer(img).normalize()

    cv2.imwrite("output.jpg",norm.read_image())

else:
    print("No image file loaded")