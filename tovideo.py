import cv2
import os
from glob import glob

def images_to_video(input_folder, output_video, fps=30):
    # 获取文件夹中所有图片的路径并排序
    img_files = sorted(glob(os.path.join(input_folder, "*.jpg")))  # 可以更改图片格式
    if not img_files:
        raise ValueError("文件夹中没有找到图片，请检查路径或图片格式。")

    # 读取第一张图片以获取图像尺寸
    first_img = cv2.imread(img_files[0])
    height, width, _ = first_img.shape

    # 设置视频编码器和输出文件
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用 mp4v 编码器
    video_writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # 将图片写入视频
    for img_file in img_files:
        img = cv2.imread(img_file)
        video_writer.write(img)  # 将图像帧写入视频

    # 释放 VideoWriter 对象
    video_writer.release()
    print(f"视频已保存至 {output_video}")

# 使用示例
input_folder = "data/super/images"  # 图片文件夹路径
output_video = "data/super/video.mp4"      # 输出视频文件名
images_to_video(input_folder, output_video)