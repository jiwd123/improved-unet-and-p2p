from tpfg import clip
import os
import cv2
path = r"E:\heng\improved_unet-main\VOCdevkit\VOC2007\Images/"
outpath = r"E:\heng\improved_unet-main\VOCdevkit\VOC2007\JPEGImages/"
# 获取该目录下所有文件，存入列表中
f = os.listdir(path)
print(len(f))

print(f[0])

n = 0
i = 0
for i in f:
    a = cv2.imread(path + f[n])
    b = f[n].strip('.jpg')
    clip(a, 1024, b, outpath)
    n=n+1
    