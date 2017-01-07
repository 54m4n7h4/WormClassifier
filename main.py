import cv2
import numpy as np
from image_loader import load_files
from image import Image, create_image_from_file
from normalizer import Normalizer
from noise_reduction import NoiseReducer
from thresholder import Thresholder
from findregion import ImageRegion


def process():
    # load in the images as Image objects
    files = load_files('raw_images')

    nameCtr = 0
    print("Iterating through files")
    print(files)
    for img in files:
        nameCtr += 1
        # Use a Histogram Normalization technique
        norm = Normalizer(img).normalize()

        #Median Noise Reduction (blurring), using kernel size of 7
        reducedNoise = NoiseReducer(norm).median_reduction(5)

        thresholded_img = Thresholder(reducedNoise).binary_threshold(50,255)

        outputimg = np.empty_like(thresholded_img.read_bright_field())
        
        # erode Image

        (bf_cntours, gfp_cntours, hierbf, hiergfp) = ImageRegion(thresholded_img,50,255).get_contours()

        cv2.drawContours(outputimg,bf_cntours,-1,(255,255,255),2)

        # Output the bright field
        cv2.imwrite("output/" + str(thresholded_img.name) + "out" + "_" + str(len(bf_cntours)) + "worms.jpg",outputimg)  
        # cv2.imwrite("threshold.jpg",thresholded_img.read_bright_field())
        cv2.imwrite("norm.jpg", norm.read_bright_field())
        
        #print("output/" + str(thresholded_img.name) + "out.jpg")
        break

if __name__ == '__main__':
    process()