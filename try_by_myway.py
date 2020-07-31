from PIL import Image
import numpy as np
import os


def dehaze_core(img: np.ndarray, windowsize=24, w0=0.6, t0=0.1):
    # axis指出取的是哪个维度上的最小值,图片(400,300,3)中,表示颜色的rgb在第三维,012的2上
    img_dark = img.min(axis=2)
    print(img_dark.shape)
    return Image.fromarray(img_dark)


if __name__ == '__main__':
    # print("请输入存储有待去雾图片文件夹的绝对路径:", end='')
    # dirpath: str = input()
    dirpath: str = r'C:\Users\Ruby\Desktop\工作区\pics'
    print(dirpath)
    for filename in os.listdir(dirpath):
        print(filename)
        img: np.ndarray = np.array(Image.open(dirpath+'\\'+filename))
        print(img.shape, type(img), sep='\n')
        img_dehaze: Image.Image = dehaze_core(img)

        img_dehaze.show()


# '''
#     C:\Users\Ruby\Desktop\工作区\pics
# '''
