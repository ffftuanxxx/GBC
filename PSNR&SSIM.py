import os
import cv2
import numpy as np
import torch
import torch.nn.functional as F
from tqdm import tqdm

def calculate_psnr(img1, img2):
    """Calculate PSNR using GPU-accelerated PyTorch."""
    mse = F.mse_loss(img1, img2)
    return 20 * torch.log10(255.0 / torch.sqrt(mse))

def calculate_ssim(img1, img2):
    """Calculate SSIM with PyTorch and GPU."""
    C1, C2 = (0.01 * 255) ** 2, (0.03 * 255) ** 2
    mu1, mu2 = img1.mean(), img2.mean()
    sigma1, sigma2 = img1.var(), img2.var()
    covariance = ((img1 - mu1) * (img2 - mu2)).mean()
    ssim = (2 * mu1 * mu2 + C1) * (2 * covariance + C2) / ((mu1 ** 2 + mu2 ** 2 + C1) * (sigma1 + sigma2 + C2))
    return ssim

def load_and_preprocess_image(image_path):
    """Load image using OpenCV and convert to PyTorch tensor on GPU."""
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = torch.tensor(img).float().permute(2, 0, 1).unsqueeze(0).cuda()  # Send to GPU
    return img

def calculate_folder_metrics(folder1, folder2):
    """Calculate average PSNR and SSIM for matching images in two folders using GPU."""
    psnr_values = []
    ssim_values = []
    common_images = set(os.listdir(folder1)) & set(os.listdir(folder2))

    for img_name in tqdm(common_images, desc=f"Processing {folder1} vs {folder2}"):
        img1_path = os.path.join(folder1, img_name)
        img2_path = os.path.join(folder2, img_name)

        # Load and preprocess images
        img1 = load_and_preprocess_image(img1_path)
        img2 = load_and_preprocess_image(img2_path)

        # Resize img1 to match img2 dimensions if needed
        if img1.shape != img2.shape:
            img1 = F.interpolate(img1, size=img2.shape[2:], mode='bilinear', align_corners=False)

        # Calculate PSNR and SSIM
        psnr_value = calculate_psnr(img1, img2).item()
        ssim_value = calculate_ssim(img1, img2).item()

        psnr_values.append(psnr_value)
        ssim_values.append(ssim_value)

    overall_psnr = np.mean(psnr_values) if psnr_values else 0
    overall_ssim = np.mean(ssim_values) if ssim_values else 0

    return overall_psnr, overall_ssim

def compare_image_folders(folders):
    """Run PSNR and SSIM comparison for each folder pair and output results."""
    for folder1, folder2, name in folders:
        overall_psnr, overall_ssim = calculate_folder_metrics(folder1, folder2)
        print(name)
        print(f"Overall PSNR for {folder1} vs {folder2}: {overall_psnr}")
        print(f"Overall SSIM for {folder1} vs {folder2}: {overall_ssim}")
        print("________________________________________________________")

if __name__ == "__main__":
    folders_to_compare = [
        ("data/lib/images", "data/lib/input", "lib color"),
        ("data/lib/input", "data/lib/inputp", "lib su"),
        ("data/lib/images", "data/lib/inputp", "lib full"),
        ("data/line2/images", "data/line2/input", "line2 color"),
        ("data/line2/input", "data/line2/inputp", "line2 su"),
        ("data/line2/images", "data/line2/inputp", "line2 full"),
        ("data/train/images", "data/train/input", "train color"),
        ("data/train/input", "data/train/inputp", "train su"),
        ("data/train/images", "data/train/inputp", "train full"),
        ("data/me/images", "data/lib/input", "me color"),
        ("data/me/input", "data/lib/inputp", "me su"),
        ("data/me/images", "data/lib/inputp", "me full")
    ]

    compare_image_folders(folders_to_compare)