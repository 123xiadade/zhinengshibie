import cv2
import numpy as np

image1 = cv2.imread(r"D:\Contest\Park1\Task1\img1.jpg")
image2 = cv2.imread(r"D:\Contest\Park1\Task1\img2.jpg")
# 假设我们已经有了视角变换矩阵 H（在实际应用中，你需要通过特征匹配等方法来估计它）
# 这里我们用一个简单的恒等矩阵作为示例，因为它不会改变图像2
H = np.float32([[1, 255, 188], [6, 213, 8], [116, 7, 1]])
# 使用warpPerspective进行图像变换
height, width, channels = image1.shape
image2_warped = cv2.warpPerspective(image2, H, (width * 2, height))
# 将原始图像1和变换后的图像2进行水平拼接（这里我们简单地将它们放在一起）
panorama = np.hstack((image1, image2_warped[:, image1.shape[1]:]))
cv2.imwrite(r"D:\Contest\Submissions\Part1\Task1\test4\img4.jpg",panorama)