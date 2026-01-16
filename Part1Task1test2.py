import cv2

image = cv2.imread(r"D:\Contest\Submissions\Part1\Task1\test1\img3.jpg")

orb = cv2.ORB_create()
# 检测关键点和计算描述符
keypoints,descriptors = orb.detectAndCompute(image,None)
# 绘制关键点
image_with_keypoints = cv2.drawKeypoints(image,keypoints,None,color=(0,255,0),flags=0)
cv2.imwrite( r"D:\Contest\Submissions\Part1\Task1\test2\keypoints_image.jpg",image_with_keypoints)
