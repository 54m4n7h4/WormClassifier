import cv2


class Image(object):
    """Class representing image files, and various methods on them"""

    def __init__(self, image):
        """Create an image from an opencv image"""
        self.image = image
        
        self.bright_field, self.gfp, _ = cv2.split(image)
        
    def read_bright_field(self):
        """Return the bright field of the image (channel 1)"""
        return self.bright_field

    def read_gfp(self):
        """Return the GFP channel of the image (channel 2)"""
        return self.gfp

    def read_image(self):
        """Get the two channels together"""
        return self.image

def create_image_from_file(filename):
    return Image(cv2.imread(filename))