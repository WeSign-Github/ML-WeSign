### Python script to split a labeled image dataset into Train, Validation, and Test folders.
# this code is from:
# Author: Evan Juras, EJ Technology Consultants
# github: https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi
# source code: https://colab.research.google.com/github/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Train_TFLite2_Object_Detction_Model.ipynb

import glob
from pathlib import Path
import random
import os

# Define paths to image folders
image_path = '/content/drive/MyDrive/CAPSTONE/Images/all/semua'
train_path = '/content/drive/MyDrive/CAPSTONE/Images/training'
val_path = '/content/drive/MyDrive/CAPSTONE/Images/validation'
test_path = '/content/drive/MyDrive/CAPSTONE/Images/test'

jpg_file_list = [path for path in Path(image_path).rglob('*.jpg')]
JPG_file_list = [path for path in Path(image_path).rglob('*.JPG')]
JPEG_file_list = [path for path in Path(image_path).rglob('*.JPEG')]
png_file_list = [path for path in Path(image_path).rglob('*.png')]

file_list = jpg_file_list + JPG_file_list + JPEG_file_list + png_file_list
file_num = len(file_list)
print('Total images: %d' % file_num)

# Determine number of files to move to each folder
train_percent = 0.8  # 80% of the files go to train
val_percent = 0.19 # 19% go to validation
test_percent = 0.01 # 1% go to test
train_num = int(file_num*train_percent)
val_num = int(file_num*val_percent)
test_num = file_num - train_num - val_num
print('Images moving to train: %d' % train_num)
print('Images moving to validation: %d' % val_num)
print('Images moving to test: %d' % test_num)

# Select 80% of files randomly and move them to train folder
for i in range(train_num):
    move_me = random.choice(file_list)
    fn = move_me.name
    base_fn = move_me.stem
    parent_path = move_me.parent
    xml_fn = base_fn + '.xml'
    os.rename(move_me, train_path+'/'+fn)
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(train_path,xml_fn))
    file_list.remove(move_me)

# Select 19% of remaining files and move them to validation folder
for i in range(val_num):
    move_me = random.choice(file_list)
    fn = move_me.name
    base_fn = move_me.stem
    parent_path = move_me.parent
    xml_fn = base_fn + '.xml'
    os.rename(move_me, val_path+'/'+fn)
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(val_path,xml_fn))
    file_list.remove(move_me)

# Move remaining files to test folder
for i in range(test_num):
    move_me = random.choice(file_list)
    fn = move_me.name
    base_fn = move_me.stem
    parent_path = move_me.parent
    xml_fn = base_fn + '.xml'
    os.rename(move_me, test_path+'/'+fn)
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(test_path,xml_fn))
    file_list.remove(move_me)