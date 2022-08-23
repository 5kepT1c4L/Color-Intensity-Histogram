import cv2 as cv
import matplotlib.pyplot as plt

img_path = input("Please input the local path of the image you want to use: ")
img = cv.imread(str(img_path))
cv.imshow('Selected Image', img)

gray_scaled_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scaled Selected Image', gray_scaled_image)

# Histogram Setup
def Histogram_graph_setup(ht):
    plt.figure()
    plt.title()
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

#Grayscale Histogram
gray_hist = cv.calcHist([gray_scaled_image], [0], None, [256], [0,256])

Histogram_graph_setup("Grayscale Histogram")
plt.plot(gray_hist)
plt.xlim(0,256)

#Color Histogram
Histogram_graph_setup("Color Histogram")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)