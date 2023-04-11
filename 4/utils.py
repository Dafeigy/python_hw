import fitz
import cv2
import numpy as np
import requests



banner_path = 'template/banner.jpg'

def pdf_to_jpg(pdf_path):

    pdfdoc=fitz.open(pdf_path)
    temp = 0

    for pg in range(pdfdoc.page_count ):
        page = pdfdoc[pg]
        temp += 1
        rotate = int(0)
        # 每个尺寸的缩放系数
        zoom_x = 0.35
        zoom_y = 0.35
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)

        pm = page.get_pixmap(matrix=trans, alpha=False)
 
        pic_name = '{}.jpg'.format(temp)
        #拼接生成pdf的文件路径
        print(pic_name)

        pm._writeIMG(f'tmp/{pic_name}',1)

def download_banner(id):
    img_url = f"http://api.k780.com/?app=barcode.get&bc_text={id}&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4"
    req = requests.get(img_url)
    with open('tmp/banner.jpg','wb') as f:
        f.write(req.content)

def make_page():
    blank = np.zeros((1042,722,3), dtype=np.uint8)
    blank[::] = 255

    banner = make_banner()
    blank[:86,:] = banner
    start_idx = 86
    for i in range(4):
        img = make_block(cv2.imread(r'tmp\1.jpg'))
        blank[start_idx:start_idx+210,46:722-46] = img
        start_idx += 245
        

    return blank

def make_block(img):
    lines = cv2.imread(r'template\lines.jpg')
    block = np.zeros((210,630,3),dtype=np.uint8)
    block[::] = 255
    block[0:209,0:295,:] = img
    
    block[0:lines.shape[0],img.shape[1]+40:630] = lines 

    # block shape: 210 x 630
    return block
    

def make_banner():
    banner_logo = cv2.imread(r'template\banner.jpg')
    print(banner_logo.shape)
    banner = np.zeros((86,722,3))
    banner[::] = 255
    banner[10:banner_logo.shape[0]+10,722-banner_logo.shape[1]-10:722-10] = banner_logo

    # banner shape: 86 x 722
    return banner



if __name__ == "__main__":
    img = cv2.imread(r'tmp\1.jpg')
    page = make_page()
    
    cv2.imshow('test',page)
    cv2.waitKey()
    # pdf_to_jpg(r'demo.pdf')