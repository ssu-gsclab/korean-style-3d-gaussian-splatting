import ffmpeg

import subprocess, sys
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-i',help="input file path")
args = parser.parse_args()  

file_path = args.i

proc1 = subprocess.Popen("cd C:/Users/tkdwn/Desktop/style_Gaussian/styleTransfer/datasets/test/images", shell=True)


proc12 = subprocess.Popen("ffmpeg -i "+ r"C:/Users/tkdwn/Desktop/style_Gaussian/input_video/"+file_path+".mp4 -qscale:v 1 -qmin 1 -vf fps=4"+" C:/Users/tkdwn/Desktop/style_Gaussian/styleTransfer/datasets/test/images"+"/%04d.png",
                        shell=True)

output = proc12.stdout.readline()
time.sleep(1000)
if proc12.poll() == None:
   proc12.kill()    

print("process kill") 


# def extract_frame(file_path,out_path):
#     ffmpeg.input(file_path).output(out_path + 'frame_%04d.png').run()

# def fps_video(video_path, output, newfps):
#     ffmpeg.input(video_path).filter('fps',fps=newfps).output(output + 'frame_%04d.png', format='png').run()

# def fps_video(file_path, output):
#     ffmpeg.input(file_path).hflip().output(output).run()

# parser = argparse.ArgumentParser() 
# parser.add_argument('-i',help="input file path")
# parser.add_argument('-o',help="1")
# args = parser.parse_args()  
# file_path = str(args.i)
# file_path = file_path.replace('\\', '/')   
# print("dddddddddddddddddddddddddddddddddddddddddddddddddddddd")
# out_path = str(args.o)
# out_path = out_path.replace('\\', '/')   

# newfps = 2
# fps_video(file_path,out_path)
# # import cv2
# import argparse


# parser = argparse.ArgumentParser() 
# parser.add_argument('-i',help="input file path")
# parser.add_argument('-o',help="1")
# args = parser.parse_args()  
# file_path = str(args.i)
# file_path = file_path.replace('\\', '/')   

# out_path = str(args.o)
# out_path = out_path.replace('\\', '/')   

# # 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
# vidcap = cv2.VideoCapture(file_path)
# frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
# frame_count -= 180


# count = 1

# while (vidcap.isOpened()):
#     # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
#     # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
#     # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
#     ret, image = vidcap.read()

#     if (int(vidcap.get(1)) % 45 == 0):
#         print('Saved frame number : ' + str(int(vidcap.get(1))))
#         cv2.imwrite(out_path+"/%04d.png" % count, image)
#         print(out_path+'/%04d.png' % count)
#         count += 1
#     if (int(vidcap.get(1)) > frame_count):
#         break

# vidcap.release()