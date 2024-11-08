import cv2
import os
from PIL import Image 
from PIL import ImageFilter
import numpy as np


# 이미지가 저장된 폴더 경로
input_folder = r'C:\Users\tkdwn\Desktop\style_Gaussian\styleTransfer\datasets\test\images_trans'
output_folder = r'C:\Users\tkdwn\Desktop\style_Gaussian\styleTransfer\datasets\test\images_dil'

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

        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6,6))
        # 팽창 연산 적용 ---②
        dst = cv2.erode(img, k)

        # dst = cv2.GaussianBlur(dst, (9, 9), sigmaX = 0, sigmaY = 0)  

        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, dst)

        print(f'{filename} laplacian saved.')

print("Done.")
