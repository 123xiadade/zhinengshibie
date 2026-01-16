import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r"D:\Contest\Park2\Task1\migong.jpg")
# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 对灰度图像进行阈值处理
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 寻找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 创建全黑图像
draw = np.zeros_like(img)
# 在全黑图像上绘制轮廓
cv2.drawContours(draw, contours, 0, (255, 0, 255), -1)
# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 19))
# 膨胀操作
dilated = cv2.dilate(draw, kernel, iterations=2)
# 腐蚀操作
eroded = cv2.erode(dilated, kernel, iterations=2)
# 计算绝对差
diff = cv2.absdiff(dilated, eroded)
# 转换为灰度图像
diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
# 寻找新的轮廓
contours2, hierarchy2 = cv2.findContours(diff_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 在原始图像上绘制新轮廓
outline = cv2.drawContours(img, contours2, 0, (0, 0, 255), -1)

cv2.imwrite(r"D:\Contest\Submissions\Part2\Task1\test5\migong.jpg",outline)