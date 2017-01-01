import cv2
import numpy as np
from image import Image, create_image_from_file
from normalizer import Normalizer
from noise_reduction import NoiseReducer

img = create_image_from_file('raw_images/1649_1109_0003_Amp5-1_B_20070424_D20_w1_066B88BE-96FA-420D-B631-F6E3CF2E71D9.tif')

if not img is None:

    norm = Normalizer(img).normalize()

    #reduce noise using a kernel of 5 x 5
    reducedNoise = NoiseReducer(norm).median_reduction(5,5)

    cv2.imwrite("normalised.jpg", norm.read_bright_field())
    cv2.imwrite("output.jpg",reducedNoise.read_bright_field())

else:
    print("No image file loaded")