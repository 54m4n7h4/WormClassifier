import glob
import cv2
import numpy as np
from image import Image, create_image_from_file
from normalizer import Normalizer
from noise_reduction import NoiseReducer
from thresholder import Thresholder
from findregion import ImageRegion


def process():
    files = []
    
    w1files = []
    w2files = []
    # go through all files, creating two lists for w1 and w2
    for file_name in glob.glob('raw_images/*_w1_*'):
        w1files.append(file_name)
    for file_name in glob.glob('raw_images/*_w2_*'):
        w2files.append(file_name)
    
    # now go through w1 files, finding the matching w2 file
    for w1file in w1files:
        file_split = w1file.split('_w1_')
        
        file_prefix = file_split[0]
        w2file = [f for f in w2files if f.startswith(file_prefix)]
        if(len(w2file) != 0):
            w2file = w2file[0]
            img = create_image_from_file(w1file,w2file,file_prefix)
            files.append(img)

    nameCtr = 0
    print("Iterating through files")
    for img in files:
        nameCtr += 1
        # Use a Histogram Normalization technique
        norm = Normalizer(img).normalize()

        #Median Noise Reduction (blurring), using kernel size of 7
        reducedNoise = NoiseReducer(norm).median_reduction(9)

        thresholded_img = Thresholder(reducedNoise).binary_threshold_inverse(90,255)

        outputimg = np.empty_like(thresholded_img.read_bright_field())
        cannygfp = cv2.Canny(thresholded_img.read_bright_field(),50,255,1)
        
        (bf_cntours, gfp_cntours, hierbf, hiergfp) = ImageRegion(thresholded_img,75,255).get_contours()

        cv2.drawContours(outputimg,bf_cntours,-1,(255,255,255),1)

        # Output the bright field
        cv2.imwrite("output/" + str(nameCtr) + "out.jpg",outputimg)  


if __name__ == '__main__':
    process()