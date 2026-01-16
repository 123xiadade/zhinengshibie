import cv2
import os

# 迷宫图像路径
maze_image_path = r"D:\Contest\Park2\Task1\migong.jpg"  # 确保路径和文件名是正确的
# 保存侵蚀后图像的路径
eroded_image_path = r"D:\Contest\Submissions\Part2\Task1\test4\maze_eroded.jpg"

# 确保保存目录存在
os.makedirs(os.path.dirname(eroded_image_path), exist_ok=True)

# 读取迷宫图像
maze_image = cv2.imread(maze_image_path)

# 如果迷宫图像是彩色的，并且我们只对某个通道（例如灰度）感兴趣，则转换为灰度图像
# maze_gray = cv2.cvtColor(maze_image, cv2.COLOR_BGR2GRAY)
# 但由于通常迷宫图像是二值化的，我们可能不需要这一步

# 定义结构元素（用于侵蚀操作）
# 你可以选择一个适当大小的结构元素，例如 3x3 的正方形
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 执行侵蚀操作
eroded_image = cv2.erode(maze_image, kernel, iterations=1)  # iterations 表示侵蚀操作的次数

# 保存侵蚀后的图像
cv2.imwrite(eroded_image_path, eroded_image)