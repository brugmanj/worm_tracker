import os
import cv2 as cv
from sklearn.model_selection import train_test_split

files = os.listdir('../wormvids/') # Creates a list of all the files to make photos from

for fil in files[5:]: # Loops through files to make photo of
    name  = '../wormvids/' + fil # Makes the name for the filepath
    print(fil) # Verification of filepath
    vid = os.path.splitext(fil)[0]

    cap = cv.VideoCapture(name) # Capturing the video based on filepath above

    if (cap.isOpened() == False): # If the capture is not open we make an error
        print(f'Error Opening {fil}')

    count = 0
    imcount =  0

    while(cap.isOpened()): # This loop steps through the video making a photo every 100 frames.
        ret, frame = cap.read()

        count += 1

        if ret == True: # This is the frame saving loop

            cv.imshow('WORMS!', frame) # Shows the frame, even if it is not captured
            
            if count % 100 == 0: # Saves every 100th frame
                cv.imwrite('../wormpics/'+ vid + '_'  + str(imcount) + '.jpg', frame)
                imcount += 1

            if cv.waitKey(25) & 0xFF == ord('q'): # Will close when 'q' key is pressed
                break

        else:
            break

    cap.release() # Ending the video and closing the window.
    cv.destroyAllWindows()
