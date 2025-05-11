# GBC: Gaussian-Based-Colorization-and-Super-Resolution-for-3D-Reconstruction
## Overview  
- Our project, GBC, takes low quality monochrome video as input and generates a high resoluted, colored 3D scene using following advanced techniques.  
## pipeline  
![main figure](main_web.jpg)

<!--## BOF-SR
![image](https://github.com/user-attachments/assets/72d75a2f-0fa1-431f-a1d2-5e24b9ed7564)

## COLMAP WORKFLOW
![image](https://github.com/user-attachments/assets/ef0ff679-0f83-4d61-808f-a36aba031d08)

## 3dgs WORKFLOW
![image](https://github.com/user-attachments/assets/a1b9ef1e-7281-42f6-9b74-4bceb5ea6174)-->


<p align="center">
  <img src="https://github.com/user-attachments/assets/72d75a2f-0fa1-431f-a1d2-5e24b9ed7564" alt="BOF-SR" width="50%" />
  
  <p align="center"><strong>Figure 1. BOF-SR</strong></p>

</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/ef0ff679-0f83-4d61-808f-a36aba031d08" alt="COLMAP Workflow" width="50%" />

  <p align="center"><strong>Figure 2. COLMAP Workflow</strong></p>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/a1b9ef1e-7281-42f6-9b74-4bceb5ea6174" alt="3DGS Workflow" width="50%" />

  <p align="center"><strong>Figure 3. 3DGS Workflow</strong></p>
</p>



<!--## Algorithm
![image](https://github.com/user-attachments/assets/77025262-a5e4-41d6-9166-d2f910baef88)-->



## DEMO
- Current demo is availabled at [GBC](http://elucidator.cn/gbc-demo/)  

## USAGE INSTRUCTIONS  
### Environment Setup
1. Download this repository:
```bash
git clone https://github.com/ffftuanxxx/GBC.git
```
2. Install dependencies:
- 2.1
```bash
conda create -n gbc python=3.10.15
conda activate gbc
pip install -r requirements.txt
cd ./the file position
```
- 2.2
  Also install 3dgs, please reference to [gaussian-splatting-Windows](https://github.com/jonstephens85/gaussian-splatting-Windows)
  
3. Download models:
- Download by `Modelscope`:
Install:
```bash
pip install modelscope
```
`method 1`: Download by SDK:
```bash
from modelscope import snapshot_download
model_dir = snapshot_download('XRailgunX/Gaussian-Based-Colorization-and-Super-Resolution-for-3D-Reconstruction')
```
`method 2`: Download by GIT:
```bash
git clone https://www.modelscope.cn/XRailgunX/Gaussian-Based-Colorization-and-Super-Resolution-for-3D-Reconstruction.git
```
4. Run the pipeline
```bash
# Please make sure you have put the model files on the right position and set the correct parameters'
PYTHONPATH=. python main.py
```

<!--Install all requirements of Gaussian-Splatting-Windows, DeOldify, Real-ESRGAN in the same environment.
Download all weight files in of Gaussian-Splatting-Windows, DeOldify, Real-ESRGAN.
You can use 480p.py to convert video to monochrome, low resolution video.
Run main.py to start whole process.-->

## Datasets
- Part of datasets are available at `modelscope`

`Method 1.` SDK
```bash
from modelscope.msdatasets import MsDataset
ds =  MsDataset.load('XRailgunX/GBC-dataset')
```

`Method 2.` GIT
```bash
git lfs install
git clone https://www.modelscope.cn/datasets/XRailgunX/GBC-dataset.git
```

## Links  
Thanks for the work of,

[gaussian-splatting-Windows](https://github.com/jonstephens85/gaussian-splatting-Windows)  \\
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
