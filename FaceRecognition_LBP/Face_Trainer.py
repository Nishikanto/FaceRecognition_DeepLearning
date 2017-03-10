import cv2
import numpy as np
from skimage import feature
from sklearn.svm import LinearSVC

numPoints = 30
radius = 8

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

def detectFace(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    largeX = 0
    largeY = 0
    largeW = 0
    largeH = 0
    for (x, y, w, h) in faces:
        # finding large rectangle
        if (w + h) > (largeW + largeH):
            largeW = w
            largeH = h
            largeX = x
            largeY = y
    cropped = None
    found = False
    try:
        img = frame.copy()
        cropped = img[largeY:largeY + largeH, largeX:largeX + largeW]
        img2 = cv2.rectangle(frame, (largeX, largeY), (largeX + largeW, largeY + largeH), (255, 0, 0), 2)
    except:
        print("error")

    if not largeW > 0:
        return None, frame
    return cropped, img2

def getimageasarray(fname):
    # print('fname=', fname)
    inputImage = cv2.imread(fname)
    face, inputImage = detectFace(inputImage)
    img = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (100, 100))
    cv2.equalizeHist(img, img)

    lbp = feature.local_binary_pattern(img, numPoints, radius, method="uniform")
    (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, numPoints + 3), range=(0, numPoints + 2))
    hist = hist.astype("float")
    hist /= (hist.sum() + 1e-7)



    ad = np.asarray(hist, dtype='float64').reshape(1, hist.size)[0]
    #print(ad)

    return ad


def loadallimages(self):
    t = []  # empty list
    # load 1-10.jpg angry images
    for i in range(19):
        fn = 'data/person1/' + str(i) + '.jpg'
        # fn=cv2.threshold(fn, 127, 255, 0)
        a = getimageasarray(fn)
        t.append(a)

    for i in range(19):
        fn = 'data/person2/' + str(i) + '.jpg'
        # fn = cv2.threshold(fn, 127, 255, 0)
        a = getimageasarray(fn)
        t.append(a)

    for i in range(19):
        fn = 'data/person3/' + str(i) + '.jpg'
        # fn = cv2.threshold(fn, 127, 255, 0)
        a = getimageasarray(fn)
        t.append(a)

    print('images loaded')
    return t


class face_train:
    def main(self):
        #print('svm tutorial')

        # load the 3 class of images
        features = loadallimages(self)
        #print(features)

        #print('svm tutorial2')
        # label the known images
        labels = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                  2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
                  3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        #print('training svm')

        print('labels=', len(labels))
        print('features', len(features))


        m = LinearSVC(C=100000.0, random_state=42) #এই লাইন টাও ওই লিন্কে দিতে বলা আছে।
        #m = svm.SVC(gamma=.01, C=1000)
        m.fit(features, labels)
        print('m=', m)
        print('training completed')
        return m