import cv2

def main():
    # 初始化摄像头
    cap = cv2.VideoCapture(0)  # 0代表默认摄像头

    # 检查摄像头是否正常打开
    if not cap.isOpened():
        print("无法打开摄像头")
        exit()

    while True:
        # 从摄像头读取一帧画面
        ret, frame = cap.read()

        # 如果读取成功，显示画面
        if ret:
            cv2.imshow('摄像头', frame)

        # 按下'q'键退出循环
        if cv2.waitKey(1) == ord('q'):
            break

    # 释放摄像头和销毁所有OpenCV窗口
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
