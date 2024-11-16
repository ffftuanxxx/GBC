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



# # 使用 ffmpeg 提取帧
# subprocess.run(
#     f"ffmpeg -i {video_input} -qscale:v 1 -qmin 1 -vf fps={fps} ./data/{output_folder_name}/inputp/%04d.jpg")
#
#
# # 使用 RealESRGAN 进行超分辨率增强
# subprocess.run(
#     f"python inference_realesrgan.py -n RealESRGAN_x4plus -i ./data/{output_folder_name}/inputp -o ./data/{output_folder_name}/input")





# 设置设备
device.set(device=DeviceId.GPU0)

# 初始化视频着色器
colorizer = get_video_colorizer()
render_factor = 21
file_name = output_folder_name
file_name_ext = file_name + '.mp4'
result_path = colorizer.colorize_from_file_name(file_name_ext, render_factor=render_factor)

