import cv2 as cv
img =  cv.imread('C:/Users/User 2/Desktop/cats.jpg')
cv.imshow('Meow', img)
cv.waitKey(0)

average = cv.blur(img, (3,3))
cv.imshow('Blurred', average)
cv.waitKey(0)

gauss = cv.GaussianBlur(img, (3,3), 0) ###Less blur than the method above
cv.imshow('Gauss', gauss)
cv.waitKey(0)

median = cv.medianBlur(img, 3) ##Less noice than average
cv.imshow('Median', median)
cv.waitKey(0)

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)