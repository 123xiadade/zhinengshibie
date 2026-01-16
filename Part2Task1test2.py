import cv2

# 迷宫图像路径
maze_image_path = r"D:\Contest\Park2\Task1\migong.jpg"
# 输出图像路径
output_dir = r"D:\Contest\Submissions\Part2\Task1\test2\maze_contours.jpg"

# 读取图像
maze_image = cv2.imread(maze_image_path)

# 转换为灰度图像
gray_image = cv2.cvtColor(maze_image, cv2.COLOR_BGR2GRAY)

# 二值化（这里使用固定阈值，你可以根据图像调整）
_, binary_image = cv2.threshold(gray_image, 17, 25, cv2.THRESH_BINARY)

# 检测轮廓（这里使用RETR_EXTERNAL仅检测最外层轮廓）
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓（在原始图像上绘制，使用白色线条，线条宽度为2）
maze_contours = cv2.drawContours(maze_image, contours, -1, (0, 255, 0), 10)
cv2.imwrite(output_dir,maze_contours)