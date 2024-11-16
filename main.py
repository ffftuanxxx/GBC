import threading
from _device import device
from device_id import DeviceId
import time
from moviepy.video.io.VideoFileClip import VideoFileClip
import subprocess
import os
import shutil
from visualize import *
import warnings
from pathlib import Path

# 用户输入参数
video_input = input("video path: ")
fps = input("fps for frames: ")
output_folder_name = input("project folder name: ")
outname = input("model output name: ")

# 创建路径
frame_path = f"./data/{output_folder_name}"
os.makedirs(frame_path, exist_ok=True)
colmappath = os.path.join(frame_path, 'input')
os.makedirs(colmappath, exist_ok=True)
input_folder_path1 = os.path.join(frame_path, 'inputp')
os.makedirs(input_folder_path1, exist_ok=True)

# 日志路径
log_path = os.path.join(frame_path, 'log.txt')

with open(log_path, "a") as log_file:
    log_file.write("extracting frames\n")
    # 使用 ffmpeg 提取帧
    subprocess.run(
        f"ffmpeg -i {video_input} -qscale:v 1 -qmin 1 -vf fps={fps} ./data/{output_folder_name}/inputp/%04d.jpg",
        shell=True, stdout=log_file, stderr=log_file)

    log_file.write("super resolution\n")
    # 使用 RealESRGAN 进行超分辨率增强
    subprocess.run(
        f"python inference_realesrgan.py -n RealESRGAN_x4plus -i ./data/{output_folder_name}/inputp -o ./data/{output_folder_name}/input",
        shell=True, stdout=log_file, stderr=log_file)

    log_file.write("colmap\n")
    # colmap
    subprocess.run(f"python convert.py -s ./data/{output_folder_name}", shell=True, stdout=log_file, stderr=log_file)

    log_file.write("colorization\n")
    # 设置设备
    device.set(device=DeviceId.GPU0)

    # 初始化视频着色器
    colorizer = get_video_colorizer()
    render_factor = 21
    file_name = output_folder_name
    file_name_ext = file_name + '.mp4'
    result_path = colorizer.colorize_from_file_name(file_name_ext, render_factor=render_factor)

    delete_path = Path("data") / file_name / "images"
    if os.path.exists(delete_path):
        shutil.rmtree(delete_path)

    old_folder_path = Path("data") / file_name / "color_images"
    new_folder_path = Path("data") / file_name / "images"
    # 重命名文件夹
    if os.path.exists(old_folder_path):
        os.rename(old_folder_path, new_folder_path)

    log_file.write("splatting\n")
    # 运行训练脚本
    subprocess.run(f"python train.py -s {frame_path} -m {outname}", shell=True, stdout=log_file, stderr=log_file)

    log_file.write("show 3D ...\n")
    subprocess.run(
        f"C:/Users/UIC/Desktop/FYP/gaussian3/gaussian-splatting-Windows/viewers/bin/SIBR_gaussianViewer_app -m C:/Users/UIC/Desktop/FYP/color/stf_color/{outname} --iterations 7000",
        shell=True, stdout=log_file, stderr=log_file)