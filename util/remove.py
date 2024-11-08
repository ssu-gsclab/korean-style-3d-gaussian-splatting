import os
import shutil
import argparse
import time

def DeleteAllFiles(filepath): #file create
    if os.path.exists(filepath):
        for file in os.scandir(filepath):
            os.remove(file.path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser() 
    parser.add_argument('-i',help="input file path")
    args = parser.parse_args()  
    file_path = str(args.i)
    file_path = file_path.replace('\\', '/')       

    #file remove
    DeleteAllFiles(file_path) 

    print("remove complete")
