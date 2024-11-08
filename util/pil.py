import cv2
import os
import numpy as np
import argparse

#원본 이미지(root) 처리

#생성 이미지(style transfer) 처리
def ImageResize(img, file_name, file_path):
    root_file_name = "root.png"
    root_path = file_path + '/root/' + root_file_name
    root_path = root_path.replace('\\', '/') 
    root = cv2.imread(root_path)
    height, width = root.shape[:2]
    read_file_path = cv2.resize(img, dsize=(width, height), interpolation=cv2.INTER_AREA) 
    img_path_retarget = file_path + '/output/input/' + file_name
    img_path_retarget = img_path_retarget.replace('\\', '/') 
    cv2.imwrite(img_path_retarget, read_file_path)

def ImageSearch(file_path) :
    image_file_path = file_path + '/input'
    possible_img_extension = ['.jpg', '.jpeg', '.JPG', '.bmp', '.png']
    for (root, dirs, files) in os.walk(image_file_path):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    # if file_name != root_path:
                    img_path = root + '/' + file_name
                    img_path = img_path.replace('\\', '/')        
                    img = cv2.imread(img_path)
                    cv2.waitKey(0)
                    print(img_path)
                    ImageResize(img, file_name, file_path)


if __name__ == '__main__':
    # file_path = r"C:\Users\tkdwn\Desktop\style_Gaussian\input_data"
    # file_path = file_path.replace('\\', '/')     

    parser = argparse.ArgumentParser() 
    parser.add_argument('-i',help="input file path")
    args = parser.parse_args()  
    file_path = str(args.i)
    file_path = file_path.replace('\\', '/')   
    ImageSearch(file_path)
    print("Pil_Image_complete")         