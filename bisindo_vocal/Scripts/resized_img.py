"""
 How to resize images
 1. open folders which contains the dataset
 2. change [input_folders] to directory you located in
 3. after the execution complete, check the new datasets

notes:
- you can resize either the original datasets or the grayscale ones, just locate
the path correctly 
- the size of resized img will reduce
"""

import cv2
import glob
import os
from pathlib import Path

input_folders = [
    r'D:\BISINDO\testing'
    #r'D:\BISINDO\A', #using original dataset. if you want to resize the grayscale img, change the directory correctly
    #r'D:\BISINDO\I',
    #r'D:\BISINDO\U',
    #r'D:\BISINDO\E',
    #r'D:\BISINDO\O'
]
output_parent_folder = r'D:\BISINDO\hasil'
os.makedirs(output_parent_folder, exist_ok=True)

#include all of img extensions
extensions = ['jpg', 'jpeg', 'JPG']

for folder in input_folders:
    output_folder = os.path.join(output_parent_folder, os.path.basename(folder))
    os.makedirs(output_folder, exist_ok=True)

    file_list = set()

    for ext in extensions:
        file_list.update(Path(folder).rglob('*.'+ ext))
    
    i = 1 #it will start count from index 1 not 0
    for file in file_list:
        img = cv2.imread(str(file))
        imgResized = cv2.resize(img, (320,320)) #resize into 320x320 pixel
        folder_name = os.path.basename(folder)[0].upper()
        output_path = os.path.join(output_folder, f'image_{folder_name}_{i}.jpg')
        cv2.imwrite(output_path, imgResized)
        i += 1
        cv2.imshow('image', imgResized)
        cv2.waitKey(30)

cv2.destroyAllWindows()