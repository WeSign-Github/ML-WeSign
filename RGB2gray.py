"""
Convert images to grayscale
How to run this code 
1. install opencv in command prompt with: pip install opencv-python
2. open this code in vscode, open folder which contains original datasets
3. change [input_folders] to your directory according the path you located in
4. after the execution is completed, check the new datasets
"""

import cv2
import os
from pathlib import Path

#list all of input folders, the code might be a bit longer
input_folders = [
    r'D:\BISINDO\A',
    r'D:\BISINDO\I',
    r'D:\BISINDO\U',
    r'D:\BISINDO\E',
    r'D:\BISINDO\O'
]
#define new directory for new datasets
output_parent_folder = r'D:\BISINDO\compressed'
os.makedirs(output_parent_folder, exist_ok=True)

#include all of image extensions
extensions = ['jpg', 'jpeg', 'JPG']

for folder in input_folders:
    output_folder = os.path.join(output_parent_folder, os.path.basename(folder))
    os.makedirs(output_folder, exist_ok=True)

    file_list = set()

    for ext in extensions:
        file_list.update(Path(folder).rglob('*.' + ext))

    i = 0
    for file in file_list:
        img = cv2.imread(str(file)) #use the str() function to convert the Path object to a string
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #change the color into grayscale
        cv2.imshow('Gray Images', gray_img)
        folder_name = os.path.basename(folder)[0].upper() #naming the files based on its correspondence folders
        output_path = os.path.join(output_folder, f'image_{folder_name}_{i}.jpg')
        cv2.imwrite(output_path, gray_img)
        i += 1
        cv2.waitKey(600) # it waits for 600 milliseconds (or 0.6 seconds)
        cv2.destroyAllWindows() #to ensure that all open windows are closed once the program execution is complete
