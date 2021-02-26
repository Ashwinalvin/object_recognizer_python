import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('ashwinrr.jfif',-1)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print('Enter F for face and E for eye')
choice = input()
if choice.upper()=='F':
    face = face_cascade.detectMultiScale(gray_img)
    for x,y,w,h in face:
       fresult = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('result',fresult)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if choice.upper()=='E':
    eye = eye_cascade.detectMultiScale(gray_img)
    for x,y,w,h in eye:
        eresult = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('result', eresult)
    cv2.waitKey(0)
    cv2.destroyAllWindows()