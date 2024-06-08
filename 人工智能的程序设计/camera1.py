import cv2

# 加载Haar级联分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image):
    # 将图像转换为灰度图，提高检测效率
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 使用Haar级联分类器检测灰度图像中的人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # 在检测到的人脸周围画矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return image

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 从摄像头读取一帧画面
    ret, frame = cap.read()
    
    # 如果读取成功，检测人脸
    if ret:
        frame = detect_faces(frame)
        cv2.imshow('Face Detection', frame)
    
    # 按下'q'键退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 释放摄像头和销毁所有OpenCV窗口
cap.release()
cv2.destroyAllWindows()
