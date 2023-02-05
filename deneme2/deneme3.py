import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import os
import math 
import numpy as np

#GREEN = (0, 255, 0)
#p2 = [100, 300]
#p3 = [200, 500]
#img = np.zeros((300, 500, 3), np.uint8)
 


# load the overlay image. size should be smaller than video frame size
imgluk = cv2.imread('luk.jpg')
imglu = cv2.imread('lu.jpg')
imgne = cv2.imread('ne.jpg')
imgnu = cv2.imread('nu.jpg')
imgo = cv2.imread('o.jpg')
imgon = cv2.imread('on.jpg')

#resize the images
size = 100
imgluk = cv2.resize(imgluk, (size, size))
imglu = cv2.resize(imglu, (size, size))
imgne = cv2.resize(imgne, (size, size))
imgnu = cv2.resize(imgnu, (size, size))
imgo = cv2.resize(imgo, (size, size))
imgon = cv2.resize(imgon, (size, size))

# Get Image dimensions
imgluk_height, imgluk_width, _ = imgluk.shape
imglu_height, imglu_width, _ = imglu.shape
imgne_height, imgne_width, _ = imgne.shape
imgnu_height, imgnu_width, _ = imgnu.shape
imgo_height, imgo_width, _ = imgo.shape
imgon_height, imgon_width, _ = imgon.shape


# Start Capture
cap = cv2.VideoCapture(0)

# Get frame dimensions
frame_width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )

detector = HandDetector(detectionCon=0.65)

# Print dimensions
print('imageluk dimensions (HxW):',imgluk_height,"x",imgluk_width)
print('imagelu dimensions (HxW):',imglu_height,"x",imglu_width)
print('imagene dimensions (HxW):',imgne_height,"x",imgne_width)
print('imagenu dimensions (HxW):',imgnu_height,"x",imgnu_width)
print('imageo dimensions (HxW):',imgo_height,"x",imgo_width)
print('imageon dimensions (HxW):',imgon_height,"x",imgon_width)
print('frame dimensions (HxW):',int(frame_height),"x",int(frame_width))

# Decide X,Y location of overlay image inside video frame. 
# following should be valid:
#   * image dimensions must be smaller than frame dimensions
#   * x+img_width <= frame_width
#   * y+img_height <= frame_height
# otherwise you can resize image as part of your code if required

xluk = 100
yluk = 10

xlu = 300
ylu = 10

xne = 500
yne = 10

xnu = 100
ynu = 150

xo = 300
yo = 150

xon = 500
yon = 150

i = 0






while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #flip the frame
    frame = cv2.flip(frame,1)
    hands, frame = detector.findHands(frame, flipType=False)


    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList = hand1["lmList"]  # List of 21 Landmark points
        #cursor= lmList[8]  # Bounding box info x,y,w,h
        #centerPoint1 = hand1['center']  # center of the hand cx,cy
        #handType1 = hand1["type"]  # Hand Type "Left" or "Right"

        length, info, frame = detector.findDistance(lmList[8][:2], lmList[12][:2], frame) #info
        #print(length)
        if length < 60:
            cursor = lmList[8]
            if xluk < cursor[0] < xluk + imgluk_width and yluk < cursor[1] < yluk + imgluk_height:
                xluk, yluk = cursor[0] - imgluk_width // 2, cursor[1] - imgluk_height // 2
            elif xlu < cursor[0] < xlu + imglu_width and ylu < cursor[1] < ylu + imglu_height:
                xlu, ylu = cursor[0] - imglu_width // 2, cursor[1] - imglu_height // 2
            elif xne < cursor[0] < xne + imgne_width and yne < cursor[1] < yne + imgne_height:
                xne, yne = cursor[0] - imgne_width // 2, cursor[1] - imgne_height // 2
            elif xnu < cursor[0] < xnu + imgnu_width and ynu < cursor[1] < ynu + imgnu_height:
                xnu, ynu = cursor[0] - imgnu_width // 2, cursor[1] - imgnu_height // 2
            elif xo < cursor[0] < xo + imgo_width and yo < cursor[1] < yo + imgo_height:
                xo, yo = cursor[0] - imgo_width // 2, cursor[1] - imgo_height // 2
            elif xon < cursor[0] < xon + imgon_width and yon < cursor[1] < yon + imgon_height:
                xon, yon = cursor[0] - imgon_width // 2, cursor[1] - imgon_height // 2

        luk = [xluk, yluk]
        on = [xon, yon]
        lu = [xlu, ylu]
        o = [xo, yo]
        nu = [xnu, ynu]
        ne = [xne, yne]
        #print(math.dist(luk, on))
        if(math.dist(luk, on) <= 125 and (xon+100 <= xluk) and math.dist(luk, lu) <= 125 and (xluk+100 <= xlu)): 
            print("onluklu %s"%i)
            i+=1
        if(math.dist(luk, on) <= 125 and (xon+100 <= xluk)): 
            print("onluk %s"%i)
            i+=1
        if(math.dist(o, nu) <= 125 and (xo+100 <= xnu) and math.dist(nu, ne) <= 125 and (xnu+100 <= xne)): 
            print("onune %s"%i)
            i+=1
        if(math.dist(o, nu) <= 125 and (xo+100 <= xnu)): 
            print("onu %s"%i)
            i+=1
        if(math.dist(o, ne) <= 125 and (xo+100 <= xne)): 
            print("one %s"%i)
            i+=1
        if(math.dist(on, luk) <= 125 and (xon+100 <= xluk)): 
            print("onluk %s"%i)
            i+=1

        #fingers1 = detector.fingersUp(hand1)
        

    
     # add image to frame
    frame[ yluk:yluk+imgluk_height , xluk:xluk+imgluk_width ] = imgluk
    frame[ ylu:ylu+imglu_height , xlu:xlu+imglu_width ] = imglu
    frame[ yne:yne+imgne_height , xne:xne+imgne_width ] = imgne
    frame[ ynu:ynu+imgnu_height , xnu:xnu+imgnu_width ] = imgnu
    frame[ yo:yo+imgo_height , xo:xo+imgo_width ] = imgo
    frame[ yon:yon+imgon_height , xon:xon+imgon_width ] = imgon

    #cv2.rectangle(img, p2, p3, GREEN, 2)
    #frame[ p2[0]:p2[0]+p2[1] , p3[0]:p3[0]+p3[1] ] = img


    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(1)

    # Exit if ESC key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()