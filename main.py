import cv2 as cv
import matplotlib.pyplot as plt

img_path = input("Please input the local path of the image you want to use: ")
img = cv.imread(str(img_path))
cv.imshow('Selected Image', img)

gray_scaled_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scaled Selected Image', gray_scaled_image)

#Grayscale Histogram
gray_hist = cv.calcHist([gray_scaled_image], [0], None, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim(0,256)
plt.show()

cv.waitKey(0)