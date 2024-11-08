import os
import argparse, sys
import time
def Ffmpeg(file_path, frame, image_type):
    #file_path = file_path.replace('\\', '/')
    #string_list = ["ffmpeg.exe -r 60.000 -i result.h264 -c:v copy", "C:/Users/tkdwn/Desktop/style_Gaussian/input_video/{}_1.mp4".format(image_type)]
    string_list = ["ffmpeg -i", file_path, "-qscale:v 1 -qmin 1 -vf", "fps={}".format(frame), r"%04d.{}".format(image_type), ">nul 2>&1"]
    read_path = " ".join(string_list)
    os.system(read_path)
    print(read_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',help="input file path")
    parser.add_argument('-f',help="video frame", default="4")
    parser.add_argument('-t',help="image type", default="png")

    args = parser.parse_args()  

    file_path = args.i
    frame = args.f
    image_type = args.t
    Ffmpeg(file_path, frame, image_type)
    print("ffmpeg complete")


