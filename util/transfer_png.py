import os
from rembg import remove 
from PIL import Image
import argparse

def image_rem(file, file_path) :
    output = remove(file)
    output.convert("RGBA").save(file_path)

def image_search(file_path) :
    possible_img_extension = ['.jpg', '.jpeg', '.JPG', '.bmp', '.png']
    for (root, dirs, files) in os.walk(file_path):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    img_path = file_path + '/' + file_name
                    img_path = img_path.replace('\\', '/')     
                    img = Image.open(img_path)
                    image_rem(img,img_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser() 
    parser.add_argument('-i',help="input file path")
    args = parser.parse_args()  
    file_path = str(args.i)
    file_path = file_path.replace('\\', '/')  
    image_search(file_path)
