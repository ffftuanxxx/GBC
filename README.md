# GBC: Gaussian-Based-Colorization-and-Super-Resolution-for-3D-Reconstruction
## Overview  
Our project, GBC, takes low quality monochrome video input and generates a high resoluted, colored 3D scene using advanced techniques.  
## pipeline  
![main figure](main_web.jpg)

## BOF-SR
![image](https://github.com/user-attachments/assets/72d75a2f-0fa1-431f-a1d2-5e24b9ed7564)

## COLMAP WORKFLOW
![image](https://github.com/user-attachments/assets/ef0ff679-0f83-4d61-808f-a36aba031d08)

## 3dgs WORKFLOW
![image](https://github.com/user-attachments/assets/a1b9ef1e-7281-42f6-9b74-4bceb5ea6174)

## Algorithm
![image](https://github.com/user-attachments/assets/77025262-a5e4-41d6-9166-d2f910baef88)



## DEMO
current demo can view at [GBC](http://elucidator.cn/gbc-demo/)  

### USAGE INSTRUCTIONS  
### Environment Setup
1. Download this repository:
```bash
git clone https://github.com/index-tts/index-tts.git
```
2. Install dependencies:
```bash
conda create -n index-tts python=3.10
conda activate index-tts
pip install -r requirements.txt
apt-get install ffmpeg
```
<!--Install all requirements of Gaussian-Splatting-Windows, DeOldify, Real-ESRGAN in the same environment.
Download all weight files in of Gaussian-Splatting-Windows, DeOldify, Real-ESRGAN.
You can use 480p.py to convert video to monochrome, low resolution video.
Run main.py to start whole process.-->

## Datasets & pretrained model
Coming soon!

## Links  
Thanks for the work of,

[gaussian-splatting-Windows](https://github.com/jonstephens85/gaussian-splatting-Windows)  
[DeOldify](https://github.com/jantic/DeOldify)
[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

## Cite
If you find GBC useful for your work please cite:
```
@article{
  author    = {Jiecheng Liao, Shi He, Yichen Yuan, Hui Zhang},
  title     = {GBC: Gaussian-Based-Colorization-and-Super-Resolution-for-3D-Reconstruction},
  conference   = {VRCAI},
  year      = {2024},
}
```

# Website License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
