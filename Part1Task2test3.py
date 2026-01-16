import cv2
import os

# 确保路径正确
input_video_path = r'D:\Contest\Park1\Task2\test3\a.mp4'
output_video_path = r'D:\Contest\Submissions\Part1\Task2\test3\a.mp4'

# 确保输出目录存在
os.makedirs(os.path.dirname(output_video_path), exist_ok=True)

# 加载面部检测分类器
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# 读取视频
cap = cv2.VideoCapture(input_video_path)

# 获取视频属性以设置输出视频的参数
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

# 创建VideoWriter对象以保存输出视频
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #pedestrians = hog.detectMultiScale(gray, 1.1, 4)
    boxes, _ = hog.detectMultiScale(gray, winStride=(4, 4), padding=(8, 8), scale=1.05)
    # 遍历检测到的行人
    for (x, y, w, h) in boxes:
        # 绘制绿色框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 计算框的中心点并绘制红色点
        center_x, center_y = x + w // 2, y + h // 2
        cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)  # 负数厚度表示填充圆形


    out.write(frame)
cap.release()
out.release()