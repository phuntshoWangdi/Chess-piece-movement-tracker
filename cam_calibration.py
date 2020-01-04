import cv2
import matlab.engine
import numpy as np
import time
import keyboard

x1=[0,75,150,225,300,375,450,525]
x2=[75,150,225,300,375,450,525,600]
y1=[0,75,150,225,300,375,450,525]
y2=[75,150,225,300,375,450,525,600]

#chessboard
#pts = [[549,122],[1070,116],[541,625],[1063,644]]
pts = [[555,121],[1080,108],[552,627],[1079,641]]
org =[(35,35),(111,34),(187,34),(262,34),(339,34),(411,34),(483,34),(566,34),
      (35,111),(111,111),(187,111),(262,111),(339,111),(411,111),(483,111),(566,111),
      (35,187),(111,187),(187,187),(262,187),(339,187),(411,187),(483,187),(566,187),
      (35,262),(111,262),(187,262),(262,262),(339,262),(411,262),(483,262),(566,262),
      (35,339),(111,339),(187,339),(262,339),(339,339),(411,339),(483,339),(566,339),
      (35,411),(111,411),(187,411),(262,411),(339,411),(411,411),(483,411),(566,411),
      (35,483),(111,483),(187,483),(262,483),(339,483),(411,483),(483,483),(566,483),
      (35,566),(111,566),(187,566),(262,566),(339,566),(411,566),(483,566),(566,566)]

cropped_img_path = 'D:/Users/Phuntsho Wangdi/Desktop/D/UT/img/'

def start_matlab_engine():
    print('Starting Matlab engine..')
    eng =  matlab.engine.start_matlab()
    print('Matlab engine started...')
    return eng

def img_cropper(img,cropped_img_path):
    img_c = 0
    #img[y:x]
    for i in range(8):    
        for j in  range(8):
            img_M = img[y1[i]:y2[i],x1[j]:x2[j]]

            cv2.imwrite(cropped_img_path+'img'+str(img_c)+'.png',img_M)
            img_c += 1

eng = start_matlab_engine()
cap=cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)

print('press \'k\' to start')
while cap.isOpened():
    key = cv2.waitKey(1)

    if keyboard.is_pressed('k'):
        print('request accepted')
        _,frame = cap.read()
        #holds the result of each chess box piece
        out = []
        counter1 = 0
        
        pts1=np.float32([pts[0],pts[1],pts[2],pts[3]])
        pts2=np.float32([[0,0],[600,0],[0,600],[600,600]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)

        c_ful_img = cv2.warpPerspective(frame,matrix,(600,600))

        #crop the full image to 64 pieces of image for prediction
        #store it in the img folder
        img_cropper(c_ful_img,cropped_img_path)

        print('Starting prediction with matlab...')
        #goes through the folders and predicts for each image
        #found in the folder
        results = eng.predicter(cropped_img_path)
        #convert matlab array to numpy array
        print('Converting to numpy array...')
        results = np.asarray(results)
        results = np.squeeze(results)
        print('Done!')
        
        time.sleep(0.3)
        for o in results:
            if o[1] >= 0.7:
                out.append(1)
            elif o[1] < 0.7:
                out.append(0)

        for i in range(64):
            f_r = cv2.putText(c_ful_img,str(out[i]),org[i],cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

        cv2.imshow('f_r',f_r)
        if key & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
