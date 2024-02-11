from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
test = cv2.imread("C:\\Users\sreenitya\Documents\PythonScripts\DIC\Images\\test8.jpg")
blur = cv2.GaussianBlur(test,(5,5),0)
gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
counts, bins, bars = plt.hist(gray.ravel(),256,[0,256])
plt.show()
shape = test.shape
print(shape)
sum = 0
divisor = 0
for i in range(256):
    sum += (256-i)*(counts[i])
    divisor += counts[i]
cutoff = (sum/divisor) + 40
print(cutoff)
new_counts = np.zeros((256,2))
for i in range(256):
    new_counts[i][0] = counts[i]
    new_counts[i][1] = i
def getcutoff(counts):
    kmeans = KMeans(n_clusters=2, random_state=0).fit(counts)
    cutoff = kmeans.cluster_centers_[0][1]
    return cutoff
new_cutoff = getcutoff(new_counts)
print(new_cutoff)
ret,bin = cv2.threshold(gray,new_cutoff,255,cv2.THRESH_BINARY_INV)
cv2.imshow("img",test)
cv2.waitKey(0)
# Noise reduction through Successive Erosion and Dilation processes or Opening
erode = cv2.erode(bin, (9, 9), iterations = 5)
dilate = cv2.dilate(erode, (9,9), iterations = 4)
cv2.imshow("img", dilate)
cv2.waitKey(0)