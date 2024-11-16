import cv2
import moviepy.editor as mp


def change_video_resolution(input_video_path, output_video_path, target_height=720):
    # 打开输入视频
    cap = cv2.VideoCapture(input_video_path)

    # 获取原始视频的宽度和高度
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 计算缩放后的宽度，保持比例
    scale_ratio = target_height / original_height
    target_width = int(original_width * scale_ratio)

    # 设置视频编码格式
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (target_width, target_height), isColor=False)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 将帧调整为目标分辨率，并转换为灰度图像
        resized_frame = cv2.resize(frame, (target_width, target_height))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        # 写入输出视频
        out.write(gray_frame)

    # 释放资源
    cap.release()
    out.release()

    print(f'视频已成功保存为: {output_video_path}')


# 示例用法
input_video = './video/color/library_line.mp4'
output_video = './video/720p/library_line1.mp4'

change_video_resolution(input_video, output_video)