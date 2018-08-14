#coding:utf-8

from glob import glob
import numpy as np
from PIL import Image

import time
import matplotlib.pyplot as plt # plt 用于显示图片
import argparse
import os
from chinese_ocr.demo import model

parser = argparse.ArgumentParser()
# Basic model parameters.
parser.add_argument('--file_path', type=str, default='test_images/test.png',
                    help='detect image')
FLAGS = parser.parse_args()
if __name__ =='__main__':
    im = Image.open(os.path.join(os.getcwd(), FLAGS.file_path))
    img = np.array(im.convert('RGB'))
    t = time.time()
    result,img,angle = model.model(img,model='keras', detectAngle=True)
    print("It takes time:{}s".format(time.time()-t))
    print("---------------------------------------")

    for key in result:
        print(result[key][1])
    plt.imshow(img)  # 显示图片
    plt.show()
