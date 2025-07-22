from PIL import Image
import numpy as np
import cv2
import os
path = r"E:\heng\improved_unet-main\VOCdevkit\VOC2007\biaoqianfenge/"
outpath = r"E:\heng\improved_unet-main\VOCdevkit\VOC2007\SegmentationClass/"
# 获取该目录下所有文件，存入列表中 只能识别8位
f = os.listdir(path)

#get_key = lambda i : int(i.split('.')[0])
#new_sort = sorted(f, key=get_key)

print(len(f))

print(f[0])

n = 0
i = 0
for i in f:
    img = cv2.imread(path + f[n]) # 填要转换的图片存储地址
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img[img<127]=0
    img[img>=127]=1

    cv2.imwrite(outpath + f[n],img) # 填转换后的图片存储地址，若在同一目录，则注意不要重名
    n=n+1
