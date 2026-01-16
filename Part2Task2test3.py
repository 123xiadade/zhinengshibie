import cv2
import os
import numpy as np


# 源图片目录
source_dir = r"D:\Contest\Park2\Task2"  # 替换为你的源图片目录
# 目标保存目录
destination_dir = r"D:\Contest\Submissions\Part2\Task2\test3"  # 确保目录存在或可以创建

# 遍历源目录中的所有文件
for filename in os.listdir(source_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):  # 仅处理图片文件
        # 读取图片
        img_path = os.path.join(source_dir, filename)
        img = cv2.imread(img_path)

        # 检查图片是否成功读取
        if img is not None:
            # 定义边界大小和类型
            top, bottom, left, right = 50, 50, 50, 50  # 例如，在所有四个方向上添加50像素的边界
            border_type = cv2.BORDER_WRAP

            # 应用边界填充
            img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, borderType=border_type)

            # 保存处理后的图片
            output_path = os.path.join(destination_dir, filename)
            cv2.imwrite(output_path, img_with_border)