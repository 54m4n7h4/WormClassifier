import cv2


class Image(object):
    """Class representing image files, and various methods on them"""

    def __init__(self, bright_field, gfp):
        """Create an image from an opencv image"""
        
        self.bright_field, self.gfp = bright_field, gfp
        
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

def create_image_from_file(filename):
    img = cv2.imread(filename)

    # now split, and remerge (gets rid of errors this way)

    bf, gfp, _ = cv2.split(img)

    # return the image
    return Image(bf, gfp)