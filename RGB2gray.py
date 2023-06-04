import  cv2
import glob
import os

#kodenya baru work per folder, bukan sekaligus gitu
os.mkdir('D:\BISINDO\compressed\A')
img_path = glob.glob('D:\BISINDO\A\*.jpg')

i = 0
for image in img_path:
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Images', gray_img)
    cv2.imwrite('D:\BISINDO\compressed\A\image_A_%i.jpg' %i, gray_img)
    i += 1
    cv2.waitKey(600)
    cv2.destroyAllWindows()
