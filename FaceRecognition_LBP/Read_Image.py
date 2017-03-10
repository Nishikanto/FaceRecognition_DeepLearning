import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)


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


class read_img:
    def main(self):
        frame = cv2.imread('data/person3.jpg')
        #ret,frame= cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        face, img = detectFace(frame)
        face2 = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        face2 = cv2.resize(face2, (100, 100))
        cv2.equalizeHist(face2, face2)
        cv2.imwrite('output.jpg', face2)