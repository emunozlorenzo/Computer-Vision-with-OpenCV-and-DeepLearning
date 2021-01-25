# Script to display a image from OpenCV

import cv2

img = cv2.imread('../../data/img/00-puppy.jpg')

w_ratio = 0.5
h_ratio = 0.5
new_img = cv2.resize(img, (0,0), img, w_ratio, h_ratio)

while True:
    cv2.imshow('Puppy', new_img)
    
    # If we've waited at least 1 ms AND we've pressed the ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()