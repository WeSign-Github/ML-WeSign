import glob
import os
import xml.etree.ElementTree as ET
import cv2
import shutil

current_directory = os.path.abspath(os.getcwd())
input_paths = glob.glob(r'/BISINDO/Compressed/resize/O/*')
output_folder = r'/BISINDO/Compressed/color_shifting/O'

def modifyXML(xml_path, file_name, file_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    filename_element = root.find('filename')
    path_element = root.find('path')
    
    filename_element.text = file_name
    path_element.text = file_path
    tree.write(xml_path)

def copyXML(src,dest):
    return shutil.copy(src, dest)

def toGrey(file_path, output_folder,output_name):
    img = cv2.imread(file_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Images', gray_img)
    output_path = os.path.join(output_folder, f'{output_name}')
    cv2.imwrite(output_path, gray_img)
    cv2.waitKey(100)
    cv2.destroyAllWindows()

def toRed(file_path, output_folder, output_name):
    img = cv2.imread(file_path)
    red_img = img.copy()
    red_img[:, :, 0] = 0  # Mengatur saluran biru (blue) menjadi 0
    red_img[:, :, 1] = 0  # Mengatur saluran hijau (green) menjadi 0
    cv2.imshow('Red Scale Images', red_img)
    output_path = os.path.join(output_folder, f'{output_name}')
    cv2.imwrite(output_path, red_img)
    cv2.waitKey(100)
    cv2.destroyAllWindows() 

def toGreen(file_path, output_folder, output_name):
    img = cv2.imread(file_path)
    red_img = img.copy()
    red_img[:, :, 0] = 0  # Mengatur saluran biru (blue) menjadi 0
    red_img[:, :, 2] = 0  # Mengatur saluran hijau (green) menjadi 0
    cv2.imshow('Red Scale Images', red_img)
    output_path = os.path.join(output_folder, f'{output_name}')
    cv2.imwrite(output_path, red_img)
    cv2.waitKey(100)
    cv2.destroyAllWindows() 

def toBlue(file_path, output_folder, output_name):
    img = cv2.imread(file_path)
    red_img = img.copy()
    red_img[:, :, 1] = 0  # Mengatur saluran biru (blue) menjadi 0
    red_img[:, :, 2] = 0  # Mengatur saluran hijau (green) menjadi 0
    cv2.imshow('Red Scale Images', red_img)
    output_path = os.path.join(output_folder,f'{output_name}')
    cv2.imwrite(output_path, red_img)
    cv2.waitKey(100)
    cv2.destroyAllWindows() 

i = 0
for file_path in input_paths:
    isXMLModified = False
    output_names = [f'O_grey_image{i}',f'O_red_image{i}',f'O_green_image{i}',f'O_blue_image{i}']
    file = os.path.splitext(file_path)
    current_ext = file[1]
    print(current_ext)
    if current_ext == ".xml":
        # Start Parse XML
        for name in output_names:
            output_xml = os.path.join(output_folder, f'{name}.xml')
            copyXML(file_path,output_xml)
            modifyXML(output_xml,f'{name}.jpg',f'{output_folder}\{name}.jpg')
        isXMLModified = True
    else:
        toGrey(file_path, output_folder,f'{output_names[0]}{current_ext}')
        toRed(file_path, output_folder,f'{output_names[1]}{current_ext}')
        toGreen(file_path, output_folder,f'{output_names[2]}{current_ext}')
        toBlue(file_path, output_folder,f'{output_names[3]}{current_ext}')
    
    if isXMLModified:
        i += 1