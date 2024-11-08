import os
import shutil
import argparse
import time

def DeleteAllFiles(filepath): #file create
    if os.path.exists(filepath):
        for file in os.scandir(filepath):
            file_name = file.path
            file_name = file_name.replace('\\', '/') 
            shutil.rmtree(file_name)

def CreateFolder1(file_path): #file remove
    create_path = file_path
    print(create_path)
    try:
        if not os.path.exists(create_path):
            os.makedirs(create_path)
    except OSError:
        print ('Error: Creating directory. ' +  create_path)

def CreateFolder(file_path, directory): #file remove
    create_path = file_path+"/"+directory
    print(create_path)
    try:
        if not os.path.exists(create_path):
            os.makedirs(create_path)
    except OSError:
        print ('Error: Creating directory. ' +  create_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser() 
    parser.add_argument('-i',help="input file path")
    parser.add_argument('-d', default="2",help="delete check")
    args = parser.parse_args()  
    file_path = str(args.i)
    delete_check = str(args.d)
    file_path = file_path.replace('\\', '/')       
    #file remove
    if delete_check == "1": DeleteAllFiles(file_path) 
    #if delete_check != "1": CreateFolder1(file_path) 
    #file create
    CreateFolder(file_path, "input") 
    CreateFolder(file_path, "output/input" )
    CreateFolder(file_path, "root")
    CreateFolder(file_path, "result/save")
    print("folder create complete")