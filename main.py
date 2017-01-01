

import cv2
import glob
from ReadImageFile import ImageFile


def process():
    files = []
    
    # go through all files in the directory, reading them into memory
    for f in glob.glob('./raw_images/'):
        files.append(ImageFile(f))
    
    cv2.namedWindow("Image Norm",cv2.WINDOW_NORMAL)
    cv2.imshow("Image Norm", files[0])


if __name__ == '__main__':
    process()