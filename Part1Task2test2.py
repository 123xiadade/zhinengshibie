import cv2
import os

# 加载面部检测分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 设置输入和输出目录
input_dir = r'D:\Contest\Park1\Task2\test2'
output_dir = r'D:\Contest\Submissions\Part1\Task2\test2'

# 遍历输入目录中的视频文件
for filename in os.listdir(input_dir):
    if filename.endswith(('.mp4', '.avi', '.mov')):  # 假设视频文件有这些扩展名
        video_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # 打开视频文件
        video = cv2.VideoCapture(video_path)

        # 设置输出视频文件的编解码器并创建VideoWriter对象
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4格式
        fps = video.get(cv2.CAP_PROP_FPS)  # 获取原视频的帧率
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while True:
            # 读取一帧
            ret, frame = video.read()
            if not ret:
                break

                # 转换为灰度图像以加快处理速度
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 面部检测
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                # 绘制蓝色矩形
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # 标注“smile”（这里假设所有面部都在微笑）
                cv2.putText(frame, 'smile', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                # 写入帧
            out.write(frame)