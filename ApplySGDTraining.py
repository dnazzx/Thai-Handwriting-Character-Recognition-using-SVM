import sys
import os
from os.path import isfile, join
import cv2
import numpy as np
import argparse

from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib


class DatasetLoad:
    def __init__(self, width=64, height=64, pre_type='Resize'):
        self.width = width
        self.height = height
        self.pre_type = pre_type

    def load(self, pathes, verbose=-1):

        datas = []
        labels = []

        mainfolders = os.listdir(pathes)

        for folder in mainfolders:
            fullpath = os.path.join(
                pathes, folder)
            listfiles = os.listdir(fullpath)

            if verbose > 0:
                print('[INFO] loading', folder, ' ...')

            for(i, imagefile) in enumerate(listfiles):
                imagepath = 'C:/Users/Strix/Desktop/Machine-Learning/project/datasets/abc/ก01/01-001.jpg'
                # pathes+'/'+folder+'/'+imagefile

                image = cv2.imread(imagepath)
                # cv2.imshow('img', image)
                print(imagepath)
                label = folder

                # if(self.pre_type == 'Resize'):
                #     image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
                datas.append(image)
                labels.append(label)
                if(verbose > 0 and i > 0 and (i+1) % verbose == 0):
                    print('[INFO] processed {}/{}'.format(i+1, len(listfiles)))
        return (np.array(datas), np.array(labels))


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", default="datasets/abc",
                help="path to input dataset")
args = vars(ap.parse_args())
pathes = args["dataset"]

width = 32
height = 32

data = DatasetLoad(width, height)

print('[INFO] loading datasets...')


label = ['01']

# label = ['01', '02', '03', '04', '05',
#          '06', '07', '08', '09', '10',
#          '11', '12', '13', '14', '15',
#          '16', '17', '18', '19', '20',
#          '21', '22', '23', '24', '25',
#          '26', '27', '28', '29', '30',
#          '31', '32', '33', '34', '35',
#          '36', '37', '38', '39', '40',
#          '41', '42', '43', '44']

datas, labels = data.load(pathes, verbose=500)
print(datas)
print(labels)
print('[INFO] shape of dates = ', datas.shape)

print('[INFO] split dataset to training and testing dataset ...')
(trainX, testX, trainY, testY) = train_test_split(
    datas, labels, test_size=0.30, random_state=45)

print(trainX)
print(testX)
print('train test X')
print(trainY)
print(testY)
le = LabelEncoder()
trainY = le.fit_transform(trainY)
testY = le.fit_transform(testY)
print(trainY)
print(testY)

model = SGDClassifier(loss='log', penalty='l2',
                      learning_rate='optimal', eta0=0.01, max_iter=1000)

print("[INFO] training...")
model.fit(trainX, trainY)

print("[INFO] evaluating classifier...")
predictions = model.predict(testX)
print(classification_report(testY, predictions, target_names=le.classes_))

joblib.dump(model, 'SGD_SVM.pkl')
