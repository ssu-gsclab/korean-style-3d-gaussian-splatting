import os
import cv2
import numpy as np
import argparse
import time

def CropImage(img_rotation) :
    crop = img_rotation[330:1744, 360:1774]
    return crop

def ImageRotation(img_path, img) :
    height, width = img.shape[:2]
    M = cv2.getRotationMatrix2D((width/4.0, height/2.0), # rotation center 
                -20, # rotation angle
                1) # image zoom
    img_rotation = cv2.warpAffine(img, M, (width, height))
    img = CropImage(img_rotation)
    cv2.imwrite(img_path, img)


def ImageSearch(file_path) :
    possible_img_extension = ['.jpg', '.jpeg', '.JPG', '.bmp', '.png']
    for (root, dirs, files) in os.walk(file_path):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    img_path = root + '/' + file_name
                    img_path = img_path.replace('\\', '/')        
                    img = cv2.imread(img_path)
                    cv2.waitKey(0)
                    ImageRotation(img_path, img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser() 
    parser.add_argument('-i',help="input file path")
    args = parser.parse_args()  
    file_path = str(args.i)
    file_path = file_path.replace('\\', '/')      
    print(file_path)
    ImageSearch(file_path) 
    print("Image rotation complete")


