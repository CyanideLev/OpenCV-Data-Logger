import cv2 as cv
import imutils as imu
import imutils.perspective as imp

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
    blur = cv.GaussianBlur(src=gray, ksize=(5,5), sigmaX=0.5)
    edge = cv.Canny(blur, 50, 200, 255)
    
    return blur, edge

#
def Feed():
    vid = cv.VideoCapture(0)

    while True:
        ret, frame = vid.read()
        if not ret:
            print('video not captured!')
            break
    
        blur, edge = canny_edge_detection(frame)
        #show live feed in new windows
        cv.imshow('original', frame)
        #cv.imshow('blur', blur)
        cv.imshow('edge', edge)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    cv.destroyAllWindows()

if __name__ == "__Feed__":
    Feed()
