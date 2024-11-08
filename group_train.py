import cv2
import os
import numpy as np
import argparse

# :: 1 = style_transfer (true 1, false 2)
# :: 2 = VR VIDEO (true 1, false 2) 
# :: 3 = ffmpeg frame num (min 1, max 10) 
# :: 4 = gaussian step (min 100, max 30000)
# :: 5 = input video name
# :: 6 = object scale gaussian (true 1, false 2)

def train(file_name):
    string_list = ["run_group_pc.bat 1 2 1 7000 ", "{}".format(file_name), " 2"]
    read_path = " ".join(string_list)
    print(read_path)
    os.system(read_path)


def ImageSearch(file_path) :
    possible_img_extension = ['.mov', '.mp4', '.avi', '.wmv','.MOV']
    for (root, dirs, files) in os.walk(file_path):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    cv2.waitKey(0)
                    train(file_name)


if __name__ == '__main__':
    # file_path = r"C:\Users\tkdwn\Desktop\style_Gaussian\input_data"
    # file_path = file_path.replace('\\', '/')     

    parser = argparse.ArgumentParser() 
    parser.add_argument('-i',default="1",help="input file path")
    args = parser.parse_args()  
    file_path = str(args.i)
    file_path = file_path.replace('\\', '/')   
    
    print(file_path)
    ImageSearch(file_path)
 