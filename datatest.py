import subprocess
import os

# 用户输入参数
video_input = input("video path: ")
fps = input("fps for frames: ")
output_folder_name = input("project folder name: ")


# 创建路径
frame_path = f"./data/{output_folder_name}"
os.makedirs(frame_path, exist_ok=True)


# 日志路径



# 使用 ffmpeg 提取帧
subprocess.run(f"ffmpeg -i {video_input} -qscale:v 1 -qmin 1 -vf fps={fps} ./data/{output_folder_name}/c/%04d.jpg")