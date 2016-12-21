import cv2


class ImageFile(object):
    """Class representing image files, and various methods on them"""
    def __init__(self, filename):
        """Read an image file from a static file on the file system"""
        self.image = cv2.imread(filename)
        self.bright_field, self.gfp = cv2.split(self.image)

    def read_bright_field(self):
        """Return the bright field of the image (channel 1)"""
        return self.bright_field

    def read_gfp(self):
        """Return the GFP channel of the image (channel 2)"""
        return self.gfp

    def read_image(self):
        """Get the two channels together"""
        return self.image
