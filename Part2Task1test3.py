import cv2
import os

# 迷宫图像路径
maze_image_path = r"D:\Contest\Park2\Task1\migong.jpg"  # 确保路径和文件名是正确的
# 保存扩展后图像的路径
output_dir = r"D:\Contest\Submissions\Part2\Task1\test3"
dilated_image_path = os.path.join(output_dir, 'maze_contours.jpg')
# 读取迷宫图像
maze_image = cv2.imread(maze_image_path)

# 定义结构元素（用于膨胀操作）
# 你可以根据需要选择一个适当大小的结构元素，例如 5x5 的正方形
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 19))
# 执行膨胀操作
dilated = cv2.dilate(maze_image, kernel, iterations=1)  # iterations 表示膨胀操作的次数

# 保存扩展后的图像
cv2.imwrite(dilated_image_path, dilated)