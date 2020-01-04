import cv2

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
while 1:
	_,frame = cap.read()

	cv2.imshow('frame',frame)
	cv2.imwrite('D:/Users/Phuntsho Wangdi/Desktop/D/UT/temp.png',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()