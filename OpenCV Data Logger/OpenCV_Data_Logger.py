import cv2 as cv

def canny_edge_detection(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(src=gray, ksize=(3,5), sigmaX=0.5)
    edge = cv.Canny(blur, 80, 145)
    
    return blur, edge

def main():
    vid = cv.VideoCapture(0)

    while True:
        ret, frame = vid.read()
        if not ret:
            print('video not captured!')
            break
    
        blur, edge = canny_edge_detection(frame)

        #cv.imshow('original', frame)
        cv.imshow('blur', blur)
        cv.imshow('edge', edge)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
