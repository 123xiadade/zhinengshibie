import cv2
import numpy as np
img1 = cv2.imread(r"D:\Contest\Park1\Task1\img1.jpg",177)
img2 = cv2.imread(r"D:\Contest\Park1\Task1\img2.jpg",177)
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
img_stacked = np.hstack((img1, img2))
# 3. 使用KNN匹配SIFT特征
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# 4. 筛选匹配点
good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)

    # 5. 绘制匹配线（在拼接前分别绘制在两张图上）
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, flags=2)

cv2.imwrite(r"D:\Contest\Submissions\Part1\Task1\test3\img3.jpg", img3)
