

import cv2
import glob
from ReadImageFile import ImageFile


def process():
    files = []
    
    # go through all files in the directory, reading them into memory
    for f in glob.glob('raw_image/*.tif'):
        f.append(ImageFile(f))



if __name__ == '__main__':
    process()