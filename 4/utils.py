import fitz
import cv2
import numpy as np

def pdf_to_jpg(name):

    pdfdoc=fitz.open(name)
    temp = 0
#     print(dir(fitz.Matrix))
    for pg in range(pdfdoc.page_count ):
        page = pdfdoc[pg]
        temp += 1
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 0.5
        zoom_y = 0.5
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
#         print(dir(page))
        pm = page.get_pixmap(matrix=trans, alpha=False)
 
        pic_name = '{}.jpg'.format(temp)
        #拼接生成pdf的文件路径
        
        print(pic_name)
#         print(dir(pm._writeIMG))
        pm._writeIMG(f'output/{pic_name}',1)

def make_blank_paper(size):
    blank = np.array(842,595,3)
if __name__ == "__main__":
    blank = np.zeros((842,595,3))
    blank[::] = 255
    cv2.imshow('test', blank)
    cv2.waitKey()
    #pdf_to_jpg(r'demo.pdf')