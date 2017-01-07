import cv2
import numpy as np
from image import Image
class KernelError(Exception):
    def __init__(self,expr,msg):
        self.expr = expr
        self.msg = msg

class NoiseReducer(object):
    def __init__(self,img):
        self.image = img

    def median_reduction(self, kernel_size):
        if(kernel_size <= 0):
            raise KernelError("The kernel must be greater than zero")
        elif(kernel_size % 2 == 0):
            raise KernelError("The kernel given must be of odd parity")
        
        bf = self.image.read_bright_field()
        gfp = self.image.read_gfp()

        # now blur
        bf = cv2.medianBlur(bf,kernel_size)
        gfp = cv2.medianBlur(gfp,kernel_size)

        return Image(bf,gfp,self.image.name)
