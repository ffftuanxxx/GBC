import os
from PIL import Image
import shutil

# 设置图片文件夹路径和备份文件夹路径
base_dir = '.\data\line2'  # 替换为您的根目录路径
images_folder = os.path.join(base_dir, 'images')
backup_folder = os.path.join(base_dir, 'color_images')

# 创建备份文件夹
os.makedirs(backup_folder, exist_ok=True)

# 遍历 images 文件夹中的所有图片文件
for filename in os.listdir(images_folder):
    file_path = os.path.join(images_folder, filename)

    # 检查文件是否为图片格式
    if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # 打开图片并转换为灰度，再转换为三通道（RGB模式）
        img = Image.open(file_path).convert('L').convert('RGB')

        # 将原始彩色图片移动到备份文件夹
        shutil.move(file_path, os.path.join(backup_folder, filename))

        # 将三通道的黑白图片保存回 images 文件夹
        img.save(file_path)

print("图片已转换为三通道黑白效果，原彩色图片已备份到 color_images 文件夹。")