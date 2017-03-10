import cv2
import dlib
import numpy as np
import sys, select, os

from skimage import feature
from sklearn import svm

from Face_Trainer import face_train
from Read_Image import read_img

win = dlib.image_window()

numPoints = 30
radius = 8


def get_img():
    read = read_img()
    read.main()


class Expression:
    def main(self):
        train = face_train()
        m = train.main()

        i = 0
        # while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            #break
            print("Break")
        i += 1

        get_img()
        a2 = cv2.imread('output.jpg', 0)

        lbp = feature.local_binary_pattern(a2, numPoints, radius, method="uniform")
        (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, numPoints + 3), range=(0, numPoints + 2))
        # normalize the histogram
        hist = hist.astype("float")
        hist /= (hist.sum() + 1e-7)

        a = np.asarray(hist, dtype='float64').reshape(1, hist.size)[0]
        print(a)
        id = m.predict(a)[0]
        print('recognized=', id)

        print('recognized: ')
        if id == 1:
            print('person1')
        elif id == 2:
            print('person2')
        elif id == 3:
            print('person3')


expression = Expression()
expression.main()
