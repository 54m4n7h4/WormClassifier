import cv2
from image import Image

class Normalizer(object):

    def __init__(self, img):
        self.image = img

    def normalize(self):
        bf = self.image.read_bright_field()
        gfp = self.image.read_gfp()

        # # normalize each one
        # grayscalebf = cv2.cvtColor(bf,cv2.COLOR_BGR2GRAY)
        # grayscalegfp = cv2.cvtColor(gfp,cv2.COLOR_BGR2GRAY)

        normalized_bf = cv2.equalizeHist(bf)
        normalized_gfp = cv2.equalizeHist(gfp)

        #cv2.imwrite("normbf.jpg", normalized_bf)
        #cv2.imwrite("normgfp.jpg",normalized_gfp)
        #cv2.imwrite("merged.jpg", cv2.merge((normalized_bf,normalized_gfp)))
        return Image(normalized_bf,normalized_gfp)

    