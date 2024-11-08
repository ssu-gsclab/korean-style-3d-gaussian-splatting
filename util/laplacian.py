import cv2
import os
from PIL import Image 
from PIL import ImageFilter
import numpy as np

std = 20

def make_noise(std, gray): 
    height, width = gray.shape 
    img_noise = np.zeros((height, width), dtype=float) 
    for i in range(height): 
        for a in range(width): 
            make_noise = np.random.normal() # 랜덤함수를 이용하여 노이즈 적용 
            set_noise = std * make_noise 
            img_noise[i][a] = gray[i][a] + set_noise 
    return img_noise

# 이미지가 저장된 폴더 경로
input_folder = r'C:\Users\tkdwn\Desktop\style_Gaussian\styleTransfer\datasets\test\images'
output_folder = r'C:\Users\tkdwn\Desktop\style_Gaussian\styleTransfer\datasets\test\images_lap'

# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 폴더 내의 모든 파일을 순회
for filename in os.listdir(input_folder):
    # 이미지 파일인지 확인 (확장자 확인)
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
         # 이미지 열기 (회색조로 불러옴)
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        # enhanced_cv_im = np.array(img) # cv2 wants a numpy array

        # 명암 대비
        alpha = -0.5
        dst = np.clip(( 1+ alpha) * img - 128 * alpha, 0, 255).astype(np.uint8)


        # 가우시안 블러 사전 적용
        #blurred_img = cv2.GaussianBlur(img, (3, 3), 3)  # 커널 크기 (3, 3)
        # blurred_img = enhanced_cv_im.filter(ImageFilter.GaussianBlur(radius=3))   
        blurred_img = cv2.GaussianBlur(img, (13, 13), sigmaX = 0, sigmaY = 0)  

        # 라플라시안 필터 적용
        laplacian = cv2.Laplacian(blurred_img, cv2.CV_64F)

        # 절대값을 취해 0~255 범위로 변환
        laplacian = cv2.convertScaleAbs(laplacian)

        # 원본 이미지에 라플라시안 결과를 더해 샤프닝 효과 적용
        sharpened_img = cv2.addWeighted(img, 2.0, laplacian, -0.5, 0)

        #img_noise = make_noise(std, sharpened_img)   
        
        # 처리된 이미지 저장
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, dst)



        print(f'{filename} laplacian saved.')

print("Done.")
