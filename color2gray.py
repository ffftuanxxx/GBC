import cv2

# 输入和输出文件路径
input_video_path = './video/color/Ruijie_HU.mp4'
output_video_path = './video/gray/Ruijie_HU.mp4'

# 打开输入视频
cap = cv2.VideoCapture(input_video_path)

# 获取视频的宽度、高度和帧率
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 设置视频编码器并创建输出视频文件
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height), isColor=False)

# 循环读取每一帧，转换为灰度，并写入输出视频
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 将彩色帧转换为灰度帧
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 写入输出视频
    out.write(gray_frame)

# 释放视频资源
cap.release()
out.release()
print("视频已成功转换为黑白！")
