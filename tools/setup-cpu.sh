conda create -n chinese-ocr python=3.6 pip scipy numpy PIL jupyter##运用conda 创建python环境
source activate chinese-ocr
pip3.6 install easydict -i https://pypi.tuna.tsinghua.edu.cn/simple/ ##选择国内源，速度更快
pip3.6 install keras==2.0.8  -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip3.6 install Cython opencv-python3.6 -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip3.6 install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip3.6 install -U pillow -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip3.6 install  h5py lmdb mahotas -i https://pypi.tuna.tsinghua.edu.cn/simple/
conda install pytorch=0.1.12 torchvision -c soumith
conda install tensorflow=1.3 ##解决cuda报错相关问题
cd ./ctpn/lib/utils
sh make-for-cpu.sh


