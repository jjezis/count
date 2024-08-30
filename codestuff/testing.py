import cv2
import random

img=cv2.imread("C:\\Users\\DistantEngouh\\OneDrive\\Desktop\\pink-polka-dots.webp")

for i in range(200):
    for j in range(img.shape[1]):
        img[i][j]=[random.randrange(255),random.randrange(255),random.randrange(255)]
cv2.imshow('flies',img)
cv2.waitKey(0)
cv2.destroyAllWindows()