import cv2 as cv
import imutils as imu

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
        cont = cont[0] if len(cont) == 2 else cont[1]
        max_cont = max(cont, key=cv.contourArea)
        #cont = imu.grab_contours(cont)
        #cont = sorted(cont, key=cv.contourArea, reverse=True)
        #displayCont = None
        
        #for c in cont:
            #peri = cv.arcLength(c, True)
            #approx = cv.approxPolyDP(c, 0.02 * peri, True)
            #if len(approx) == 4:
                #displayCont = approx
        
        contour_vid = vid.read()
        cv.drawContours(contour_vid,[max_cont],0,(0,255,0),2)       
        #show live feed in new windows
        cv.imshow('original', frame)
        #cv.imshow('blur', blur)
        cv.imshow('edge', edge)
        cv.imshow('contour', contour_vid)        

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
