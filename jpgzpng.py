# 图片格式转换, jpg转png
 
# 方法一
 
from PIL import Image
 
img = Image.open('test.jpg')
img.save('test1.png')
 
 
# 方法二
 
from cv2 import imread, imwrite
 
image = imread("test.jpg", 1)
imwrite("test2.png", image)