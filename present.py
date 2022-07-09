import cv2 as cv 
import numpy as np

img=cv.imread('Photos\Ryan.jpg')

cv.imshow('jar jar',img)
cv.waitKey(0)

img[img.shape[0]//2][img.shape[1]//2]=[255,0,0]

cv.imshow('pixel',img) 
cv.waitKey(0)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.waitKey(0)

blur = cv.GaussianBlur(img, (5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
cv.waitKey(0)

canny = cv.Canny(img, 1, 200)
cv.imshow('canny',canny)
cv.waitKey(0)

canny = cv.Canny(blur,1,200)
cv.imshow('canny',canny)
cv.waitKey(0)

dilated = cv.dilate(img,(3,3),iterations=20)
cv.imshow('dilate',dilated)
cv.waitKey(0)

eroded= cv.erode(dilated,(3,3),iterations=20)
cv.imshow('Eroded',eroded)
cv.waitKey(0)

cropped = img[img.shape[0]//2:img.shape[0], img.shape[1]//2:img.shape[1]]
cv.imshow('cropped', cropped)
cv.waitKey(0)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
cv.waitKey(0)

for row in range(img.shape[0]):
    for col in range(img.shape[1]): 
          img[row, col]=[255,255,255]
cv.imshow('pixel',img)
cv.waitKey(0)

img=cv.imread('Photos\jar-jar-lightsaber2.jpg')

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
cv.waitKey(0)

blank[200:300,300:400]=[0,0,255]
cv.imshow('Green',blank)
cv.waitKey(0)

blank = np.zeros((500,500,3),dtype='uint8')

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('rectangle',blank)
cv.waitKey(0)

blank = np.zeros((500,500,3),dtype='uint8')

cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
cv.imshow('rect',blank)
cv.waitKey(0)

blank = np.zeros((500,500,3),dtype='uint8')

cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.imshow('circ', blank)
cv.waitKey(0)

blank = np.zeros((500,500,3),dtype='uint8')

cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
cv.imshow('line',blank)
cv.waitKey(0)

blank = np.zeros((500,500,3),dtype='uint8')

cv.putText(blank,'Hello',(img.shape[1]//2,img.shape[0]//2),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
cv.imshow('text', blank)
cv.waitKey(0)

cv.circle(img,(img.shape[1]//2,img.shape[0]//2),40,(255,255,255),thickness=3)
cv.imshow('cat',img)
cv.waitKey(0)


capture=cv.VideoCapture(0)

while True:
    isTrue, frame =capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break

capture.release()

#destroys the window

cv.destroyAllWindows