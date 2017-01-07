import cv2
import re
import os

class Image(object):
    """Class representing image files, and various methods on them"""

    def __init__(self, bright_field, gfp, name):
        """Create an image from an opencv image"""
        
        self.bright_field, self.gfp = bright_field, gfp
        self.name = name #set the name of the image
        
    def read_bright_field(self):
        """Return the bright field of the image (channel 1)"""
        return self.bright_field

    def read_gfp(self):
        """Return the GFP channel of the image (channel 2)"""
        return self.gfp
    

    # def read_image(self):
    #     """Get the two channels together"""
    #     img = []
    #     img[:] = self.bright_field[:] + self.gfp[:]
    #     return img

def create_image_from_file(filename_bf, filename_gfp,name):
    img_bf = cv2.imread(filename_bf)
    img_gfp = cv2.imread(filename_gfp)
    # now split, and remerge (gets rid of errors this way)

    bf, _ , _ = cv2.split(img_bf)
    gfp, _, _ = cv2.split(img_gfp)

    # return the image
    return Image(bf, gfp, name)