import cv2
import os

# 加载分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 读取图片目录
image_dir = r"D:\Contest\Park1\Task2\test1"
output_dir = r"D:\Contest\Submissions\Part1\Task2\test1"
# 遍历目录中的每张图片
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # 假设图片是jpg或png格式
        img_path = os.path.join(image_dir, filename)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 检测人脸
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 绘制绿色矩形框

            # 在检测到的人脸区域内检测眼睛
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)  # 绘制红色矩形框
        output_filename = os.path.join(output_dir, filename)
        cv2.imwrite(output_filename, img)