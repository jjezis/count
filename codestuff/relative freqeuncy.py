import cv2
img=cv2.imread("C:\\Users\\DistantEngouh\\OneDrive\\Pictures\\Screenshot_20220816-083656.png")
w=100
h=100
resize=(w,h)
resized=cv2.resize(resize,interpolation=cv2.INTER_LINEAR)

cv2.imwrite('things',resized)
cv2.imshow('things',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()