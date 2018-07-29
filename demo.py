#coding:utf-8
import model
from glob import glob
import numpy as np
from PIL import Image
import time
import matplotlib.pyplot as plt # plt 用于显示图片
paths = glob('./test/*.*')

if __name__ =='__main__':
    im = Image.open("./test/test.png")
    img = np.array(im.convert('RGB'))
    t = time.time()
    result,img,angle = model.model(img,model='keras', detectAngle=True)
    print("It takes time:{}s".format(time.time()-t))
    print("---------------------------------------")

    for key in result:
        print(result[key][1])
    plt.imshow(img)  # 显示图片
    plt.show()