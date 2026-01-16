import cv2

# 读取迷宫图像
input_path = cv2.imread(r"D:\Contest\Park2\Task1\migong.jpg",cv2.IMREAD_GRAYSCALE) # 假设迷宫图像的文件名为 maze_image.jpg
output_path = r"D:\Contest\Submissions\Part2\Task1\test1\migong.jpg"

_, binary = cv2.threshold(input_path, 27, 155, cv2.THRESH_BINARY)

cv2.imwrite(output_path, binary)
