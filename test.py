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

    cannygfp = cv2.Canny(thresholded_img.read_bright_field(),50,200,3)
    outputimg = np.zeros_like(cannygfp)
    min_line_length = 5
    max_line_gap = 20
    lines = cv2.HoughLinesP(cannygfp,1,np.pi/45,20,min_line_length,max_line_gap)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        print(x1, ",",y1," to ",x2,",",y2)
        cv2.line(outputimg,(x1,y1),(x2,y2), (255,255,255),1)

    # Output the bright fields
    cv2.imwrite("normalised.jpg", norm.read_gfp())
    cv2.imwrite("output.jpg",outputimg)
else:
    print("No image file loaded")