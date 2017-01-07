import cv2
import numpy as np
from image import Image, create_image_from_file
from normalizer import Normalizer
from noise_reduction import NoiseReducer
from thresholder import Thresholder
from findregion import ImageRegion

img = create_image_from_file('raw_images/1649_1109_0003_Amp5-1_B_20070424_D20_w1_066B88BE-96FA-420D-B631-F6E3CF2E71D9.tif')

if not img is None:

    # Use a Histogram Normalization technique
    norm = Normalizer(img).normalize()

    #Median Noise Reduction (blurring), using kernel size of 7
    reducedNoise = NoiseReducer(norm).median_reduction(7)

    thresholded_img = Thresholder(reducedNoise).binary_threshold_inverse(75,255)

    outputimg = np.empty_like(thresholded_img.read_bright_field())
    cannygfp = cv2.Canny(thresholded_img.read_bright_field(),50,255,1)
    
    (bf_cntours, gfp_cntours, hierbf, hiergfp) = ImageRegion(thresholded_img,75,255).get_contours()
    print(hierbf[0])
    print(len(gfp_cntours))
    cv2.drawContours(outputimg,bf_cntours,-1,(255,255,255),1)

    # Output the bright fields
    cv2.imwrite("normalised.jpg", norm.read_gfp())
    cv2.imwrite("output.jpg",outputimg)
else:
    print("No image file loaded")

# todo: use hierarchy in contours to work out the smaller items