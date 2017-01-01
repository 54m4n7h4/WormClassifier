import cv2
import numpy as np
from image import Image

class NoiseReducer(object):
    def __init__(self,img):
        self.image = img

    def median_reduction(self, kernel_x, kernel_y):
        bf = self.image.read_bright_field()
        gfp = self.image.read_gfp()

        kernel = np.ones((kernel_x, kernel_y),np.uint8)
        # now blur
        bf = cv2.medianBlur(bf,5)
        gfp = cv2.medianBlur(gfp,5)

        return Image(bf,gfp)
