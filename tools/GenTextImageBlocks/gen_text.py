#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------
# GenTextBlocks
# Copyright (c) 2017 VisInt
# Licensed under The MIT License [see LICENSE for details]
# Written by Wenyuan Xue
# --------------------------------------------------------

import cv2
import os
import sys
import pprint
import argparse
import lib.IOUtils as IOUtils
from lib.templateImage import TemplateImage
from lib.textImageGenerater import TextImageGenerater
from lib.config import cfg, cfg_from_file

def parse_args():
  """
  Parse input arguments
  """
  parser = argparse.ArgumentParser(description='Generate block images(single line text) \
        for OCR training.')
  parser.add_argument('--cfg', dest='cfg_file',
                      help='data path config file',
                      default="./cfg.yml", type=str)
  parser.add_argument('--imgType', dest='Pure_or_Noise',
                      help='type of generated images',
                      default='Pure', type=str)
  parser.add_argument('--noiseMode', dest='Template_or_Imgaug',
                      help='mode to add noise ',
                      default="Template", type=str)

#  if len(sys.argv) == 1:
#    parser.print_help()
#    sys.exit(1)

  args = parser.parse_args()
  return args

if __name__ == '__main__':
    args = parse_args()
    print('Called with args:')
    print(args)

    if args.cfg_file is not None:
        cfg_from_file(args.cfg_file)

    print('Using config:')
    pprint.pprint(cfg)
    file_path = cfg.SOURCE.TEXTS_PATH
    files = os.listdir(file_path)
    for file in files:
        text_path = os.path.join(file_path, file)
        imageBlock = TextImageGenerater(cfg.SOURCE.FONT_PATH, cfg.SCALES, cfg.DEGREES)
        textImages, textCharLabels = imageBlock.GenerateImgs( \
            text_path, args.Pure_or_Noise, args.Template_or_Imgaug)
        savingPath = os.path.join(cfg.SAVE.IMAGE_PATH, args.Pure_or_Noise)
        IOUtils.SaveData(savingPath, textImages, textCharLabels)

    print('Done.')
