import cv2
import numpy as np
from image import Image
# this will input a canny image
# log locations of pixels with a given color
# then, take a walk around the graph of connected pixels

class ImageRegion(object):
    def __init__(self,image,thresh1, thresh2):
        bf = image.read_bright_field()
        gfp = image.read_gfp()

        kernel = np.ones((7,7),np.uint8)

        # erode
        #bf = cv2.dilate(bf,kernel,iterations=1)
        #gfp = cv2.dilate(gfp,kernel,iterations=1)

        bf = cv2.morphologyEx(bf,cv2.MORPH_CROSS,kernel)
        gfp = cv2.morphologyEx(gfp,cv2.MORPH_CROSS,kernel)

        bf = cv2.morphologyEx(bf,cv2.MORPH_GRADIENT,kernel)
        gfp = cv2.morphologyEx(gfp,cv2.MORPH_GRADIENT,kernel)


        bf = cv2.Canny(bf,thresh1,thresh2,2)
        gfp = cv2.Canny(gfp,thresh1, thresh2,2)

        self.image = Image(bf,gfp,image.name)
    
    def get_contours(self):
        # find contours
        _, contoursbf, hierarchybf = cv2.findContours(self.image.read_bright_field(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        _, contoursgfp, hierarchygfp = cv2.findContours(self.image.read_gfp(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        return (contoursbf, contoursgfp, hierarchybf, hierarchygfp)