import cv2
from image import Image
# The _ is used here to ignore the 'retValue' yielded from the threshold
# as we don't need to use it with global thresholding.
class Thresholder(object):
    def __init__(self,img):
        self.img = img

    def __threshold(self,img,trig,maxVal,flag):
        _ , thresholded = cv2.threshold(img,trig,maxVal,flag)
        return thresholded

    def binary_threshold(self,trig,maxVal):
        bf = self.__threshold(self.img.read_bright_field(),trig,maxVal,cv2.THRESH_BINARY)
        gfp = self.__threshold(self.img.read_gfp(),trig,maxVal,cv2.THRESH_BINARY)

        return Image(bf,gfp)

    def binary_threshold_inverse(self,trig,maxVal):
        bf = self.__threshold(self.img.read_bright_field(),trig,maxVal,cv2.THRESH_BINARY_INV)
        gfp = self.__threshold(self.img.read_gfp(),trig,maxVal,cv2.THRESH_BINARY_INV)

        return Image(bf,gfp)
        
    def truncate_threshold(self,trig,maxVal):
        bf = self.__threshold(self.img.read_bright_field(),trig,maxVal,cv2.THRESH_TRUNC)
        gfp = self.__threshold(self.img.read_gfp(),trig,maxVal,cv2.THRESH_TRUNC)

        return Image(bf,gfp)

    def zero_threshold(self,trig,maxVal):
        bf = self.__threshold(self.img.read_bright_field(),trig,maxVal,cv2.THRESH_TOZERO)
        gfp = self.__threshold(self.img.read_gfp(),trig,maxVal,cv2.THRESH_TOZERO)

        return Image(bf,gfp)
    
    def zero_threshold_inverse(self,trig,maxVal):
        bf = self.__threshold(self.img.read_bright_field(),trig,maxVal,cv2.THRESH_TOZERO_INV)
        gfp = self.__threshold(self.img.read_gfp(),trig,maxVal,cv2.THRESH_TOZERO_INV)

        return Image(bf,gfp)