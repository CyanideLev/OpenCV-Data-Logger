import cv2 as cv
import imutils as imu
import numpy as nu

Digit_Table = { 
    
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 1, 0): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9
    
}

def canny_edge_detection(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(src=gray, ksize=(5,5), sigmaX=0)
    edge = cv.Canny(blur, 50, 200, 255)
    
    return blur, edge

#
def main():
    vid = cv.VideoCapture(0)

    while True:
        ret, frame = vid.read()
        if not ret:
            print('video not captured!')
            break
        
        blur, edge = canny_edge_detection(frame)
        cont = cv.findContours(edge.copy(), cv.RETR_EXTERNAL,
            cv.CHAIN_APPROX_SIMPLE)
        cont = imu.grab_contours(cont)
        cont = sorted(cont, key=cv.contourArea, reverse=True)
        displayCont = None
      
        #while True:
            #ret, frame = vid.read()
            #if not ret:
                #print('video not captured!')
                #break
            #for c in cont:
            #peri = cv.arcLength
            #approx = cv.approxPolyDP(c, 0.02 * peri)
            #if len(approx) == 4:
                #displayCont = approx
                #break
            #return displayCont
        #print(displayCont)   
        #cv.drawContours(cont, displayCont , 0, (0,255,0), 3)       
        #show live feed in new windows 
        cv.imshow('original', frame)
        #cv.imshow('blur', blur)
        cv.imshow('edge', edge)
        #cv.imshow('contour', cont)        
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
