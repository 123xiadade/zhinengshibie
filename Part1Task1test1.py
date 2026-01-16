import cv2
import numpy as np

img1 = cv2.imread(r"D:\Contest\Park1\Task1\img1.jpg")
img2 = cv2.imread(r"D:\Contest\Park1\Task1\img2.jpg")
combin_img = np.hstack((img1, img2))
cv2.imwrite(r"D:\Contest\Submissions\Part1\Task1\test1\img3.jpg",combin_img)
