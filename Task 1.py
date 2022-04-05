import cv2 as cv
# image = cv.imread('Tutorials/images/plant.jpeg') #image path
# cv.imshow(winname='plant', mat=image)  #displays the image in another window
# cv.waitKey(0)

video_location = 0 #video location is the webcam
try:
    capture = cv.VideoCapture(video_location)   

    while True:
        isTrue, frame = capture.read()  

        frame_grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow(winname='original', mat=frame) #images shown by each frame 
        cv.imshow(winname='greyscale', mat=frame_grey)
        if cv.waitKey(20) & 0xFF == ord('x'):      #exit the window pressing the 'x' key
            break
    capture.release()      
    cv.destroyAllWindows()  
except:
    print('error')