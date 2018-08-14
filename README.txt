准备：
angle model: 下载地址https://pan.baidu.com/s/1zquQNdO0MUsLMsuwxbgPYg    存入angle目录下
ctpn model: 下载https://pan.baidu.com/s/1aT-vHgq7nvLy4M_T6SwR1Q#list/path=%2F   放入ctpn/models目录下

训练Step4:
1.执行脚本、抓取网站数据（名著小说网站）tools/fetch_data/fetchmingzhuxiaoshuo.py
2.执行脚本、生成数据样本 tools/GenTextImageBlocks/gen_text.py
3.执行脚本、创建数据集 tools/create_dataset/create_dataset.py
4.执行脚本、训练数据集 train/keras-train/trainbatch.py

预测Step1:
执行脚本、预测 demo.py

来源于一下分支：
https://github.com/jiangxiluning/chinese-ocr
https://github.com/uid00000000/chinese-ocr-modify.git
