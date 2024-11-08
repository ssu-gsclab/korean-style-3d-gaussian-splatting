import cv2
import os
from PIL import Image 
from PIL import ImageFilter
import numpy as np
import argparse



parser = argparse.ArgumentParser() 
parser.add_argument('-i',default="1",help="input file path")
args = parser.parse_args()  
file_path = str(args.i)
file_path = file_path.replace('\\', '/')   

# 이미지가 저장된 폴더 경로
input_folder = r'C:\Users\tkdwn\Desktop\style_Gaussian\styleTransfer\datasets\test\images_final'
output_folder = file_path
#output_folder = r'C:\Users\tkdwn\Desktop\style_Gaussian\output_data\Car_2_test.mp4\input'

# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 폴더 내의 모든 파일을 순회
for filename in os.listdir(input_folder):
    # 이미지 파일인지 확인 (확장자 확인)
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
         # 이미지 열기 (회색조로 불러옴)
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        # 팽창 연산 적용 ---②
        dst = cv2.erode(img, k)
        blurred_img = cv2.GaussianBlur(dst, (5, 5), sigmaX = 0, sigmaY = 0)  
        # dst = cv2.GaussianBlur(dst, (9, 9), sigmaX = 0, sigmaY = 0)  

        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, blurred_img)

        print(f'{filename} laplacian saved.')

print("Done.")
