import cv2
import glob
import os

#kodenya baru work per folder, bukan sekaligus gitu
input_files = 'D:\BISINDO\compressed\A'
os.mkdir('D:\BISINDO\converted\A')

i=1

for img in glob.glob(input_files + "\*.jpg"):
    image = cv2.imread(img)
    imgResized = cv2.resize(image, (320,320))
    cv2.imwrite("D:\BISINDO\converted\A\Image_A_%i.jpg" %i, imgResized)

    i += 1
    cv2.imshow('image', imgResized)
    cv2.waitKey(30)

cv2.destroyAllWindows()