import cv2
import numpy as np
from image import Image, create_image_from_file
from normalizer import Normalizer
from noise_reduction import NoiseReducer
from thresholder import Thresholder

img = create_image_from_file('raw_images/1649_1109_0003_Amp5-1_B_20070424_D20_w1_066B88BE-96FA-420D-B631-F6E3CF2E71D9.tif')

if not img is None:

    # Use a Histogram Normalization technique
    norm = Normalizer(img).normalize()

    #Median Noise Reduction (blurring), using kernel size of 7
    reducedNoise = NoiseReducer(norm).median_reduction(7)

    thresholded_img = Thresholder(reducedNoise).binary_threshold_inverse(50,255)

    # Output the bright fields
    cv2.imwrite("normalised.jpg", norm.read_gfp())
    cv2.imwrite("output.jpg",thresholded_img.read_gfp())
else:
    print("No image file loaded")