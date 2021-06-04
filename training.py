import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import joblib
# import glob
# from PIL import Image
# image_list = []


dir = 'C:\\Users\\Strix\\Desktop\\Machine-Learning\\project\\datasets'

categories = ['ก01', 'ข02', 'ฃ03', 'ค04', 'ฅ05',
              'ฆ06', 'ง07', 'จ08', 'ฉ09', 'ช10',
              'ซ11', 'ฌ12', 'ญ13', 'ฎ14', 'ฏ15',
              'ฐ16', 'ฑ17', 'ฒ18', 'ณ19', 'ด20',
              'ต21', 'ถ22', 'ท23', 'ธ24', 'น25',
              'บ26', 'ป27', 'ผ28', 'ฝ29', 'พ30',
              'ฟ31', 'ภ32', 'ม33', 'ย34', 'ร35',
              'ล36', 'ว37', 'ศ38', 'ษ39', 'ส40',
              'ห41', 'ฬ42', 'อ43', 'ฮ44']

data = []

for category in categories:
    path = os.path.join(dir, category)
    label = categories.index(category)

    for img in os.listdir(path):
        imgpath = os.path.join(path, img)
        font_img = cv2.imread(imgpath, 0)
        # print(font_img)
        try:
            font_img = cv2.resize(font_img, (50, 50))
            image = np.array(font_img).flatten()

            data.append([image, label])
        except Exception as e:
            pass

print(data)
