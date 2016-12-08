import cv2
import numpy


class ImageFile(object):
    def __init__(self, filename):
        self.image = cv2.imread(filename)

    def read_bright_field(self):
        # first channel
        pass

    def read_gfp(self):
        pass
