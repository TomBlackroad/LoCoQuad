import cv2
 
# Opens the Video file
cap= cv2.VideoCapture('/home/mbl/Documents/LoCoQuad/Code/Captures/2020-03-29--22-05-46.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('kang'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()
