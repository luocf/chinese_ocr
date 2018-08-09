#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------
# GenTextBlocks
# Copyright (c) 2017 VisInt
# Licensed under The MIT License [see LICENSE for details]
# Written by Siqi Cai and Wenyuan Xue
# --------------------------------------------------------

import os
import cv2
import logging

logging.basicConfig(level=logging.INFO)

def GetFilesList(pathToImage):
    ret = []
    for rt, dirs, files in os.walk(pathToImage):
        for filename in files:
            ret.append(filename)
    return ret

def LoadTexts(textPath):
    f = open(textPath,'r')
    texts = f.read()
    texts = str(texts)
    texts = texts.replace(' ','').replace('\r','').strip('\n').split('\n')
    textsList = []
    for line in texts:
        textsList.append(line)
    return textsList

def IsImage(filePath):
    strs = filePath.split('.')
    format = strs.pop()
    if format == 'png' or format == 'jpg':
        return True
    else:
        return False

def SaveData(savePath, images, charLabels, filesPerDir = 10000):
    logging.info("Saving Data. Total: %d images", len(images))

    imgLength = len(images)

    for ind in range(imgLength):
        dirName = str(ind/filesPerDir)
        path = savePath#os.path.join(savePath,dirName)
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info("Saving Data. Make directory: "+path)
        imgFile        = os.path.join(path,str(ind)+".jpg")
        charLabelsFile = os.path.join(path,str(ind)+".txt")
        #save image
        cv2.imwrite(imgFile, images[ind])
        #save charLabels
        cf = open(charLabelsFile, 'w')
        cf.write(str(charLabels[ind]))
        cf.close()
        percentage = int(ind*100.0/(imgLength*1.0))
        if percentage % 5 == 0:
            logging.info("Saving Data. Saving, %d %%", percentage)
    logging.info("Saving Data. Saving Done.")
    return True

#def saveImages(matList, nameList, savePath):

    #return True

def saveText(textList, nameList, savePath):
    assert (len(textList) == len(nameList) ), \
        "The number of textList don't equal to nameList."
    for i in range(len(textList)):
        f=open(savePath+'/'+nameList[i],'w')
        f.write(textList[i])
        f.close()
    return True


def LoadTemplate(templatePath):
    f = open(templatePath,'r')
    templateText = f.read().strip('\n').split('\n')
    templateList = []
    for line in templateText:
        line = line.replace('\n','').replace('\r','').strip(' ').split(' ')
        templateList.append((float(line[0]),min(20.0,float(line[1])),float(line[2]),min(10.0,float(line[3]))))
    return templateList

def LoadDict(dictPath):
    f = open(dictPath,'r')
    dictText = f.read()
    dictText = str(dictText)
    dictText = dictText.strip('\n').split('\n')
    charDict = {0:' '}
    for line in dictText:
        line = line.replace('\n','').replace('\r','').strip(' ').split(' ')
        charDict[int(line[0])] = line[1]
    return charDict
