import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

# This code outlines each worm, and tries to seperate them from each other

files = os.listdir('REDACTED')


for fil in files:
    print('../wormvids/' + fil)
    cap = cv.VideoCapture('../wormvids/' + fil)

    if (cap.isOpened() == False):
        print('Error opening video')

    count = 1

    while(cap.isOpened()):
        
        ret, frame = cap.read()
        count += 1
        if (ret == True) & (count %2 ==0): # Goes through every other frame
            capbw = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # Converts the video to black and white

            ret, thresh = cv.threshold(capbw, 127, 255, 0) # Makes a threshold for contours.
            _, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # Finds all contours based off the threshold above

            areas = []
            centers = []

            for contour in contours: # Goes through each contour and removes all with area less than 1000 and greater than 5000
                if (cv.contourArea(contour) >  1000) & (cv.contourArea(contour) < 5000):
                    areas.append(contour)
                    M = cv.moments(contour) # This makes a center dot based off the contour
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    centers.append((cX, cY))
                    rect = cv.minAreaRect(contour)
                    box = cv.boxPoints(rect)
                    box = np.int0(box)
                    im = cv.drawContours(frame, [box],0,(0,0,255),2)

            cv.drawContours(frame, areas, -1, (0,255,0), 2) # Draws the contour on the image in bright green
            for circle in centers:
                cv.circle(frame, circle, 7, (0,255,0), -1) # Draws the center as a dot
                cv.imshow('cleaner???', frame) # Shows the resulting image
            if cv.waitKey(25) & 0xFF == ord('q'): # Quits when 'q' is pressed
                break
        elif ret == True: # Skips if count is not mod 2.
            pass
        else: # Breaks if there is an error
            break

    cap.release()
    cv.destroyAllWindows()
