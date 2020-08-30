import cv2
import sys
 
# Opens the Video file
cap= cv2.VideoCapture(sys.argv[1])
i=1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    location = str(sys.argv[2]) + 'frame_' + str(i) + '.jpg'
    cv2.imwrite(location, frame)
    i+=1
 
print("\/\DONE/\/")
cap.release()
cv2.destroyAllWindows()
