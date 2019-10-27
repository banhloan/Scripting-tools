import os
import shutil 
from PIL import Image
import glob

dirpath = os.getcwd()

def createFolder(dirpath):
    try:
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
    except OSError:
        print ('Error: Creating directory. ' +  dirpath)

def check_image_with_pil(imagePath):
    try:
        Image.open(imagePath)
        shutil.move(imagePath,'./Pictures/')   
    except (IsADirectoryError,IOError):
        pass

def main():
    createFolder('./Pictures/')
    toCheck = os.listdir(dirpath)
    for item in toCheck:
        fullPath = dirpath + "/" + item
        # print(fullPath)
        check_image_with_pil(fullPath) 
    
if __name__ == "__main__":
    main()
    

