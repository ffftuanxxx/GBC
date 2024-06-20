@echo off

REM Step 1: Create an 'input' folder in the specified ffmpeg_path
mkdir %1\input

REM Step 2: Convert video to images using ffmpeg
ffmpeg -i %1/%2 -qscale:v 1 -qmin 1 -vf fps=%3 %1/input/%%04d.jpg

REM Step 2.5: Change directory to ffmpeg_path and then go up two levels
cd %1
cd ..
cd ..

REM Step 3: Run Python script convert.py
python convert.py -s %1

REM Step 4: go back to FYP
cd ..
cd ..
cd vision_changing/iv

REM Step 5: images to video
python itv.py %1/images

REM Step 6: Copy a file from one path to another
cd ..
cd ..
copy C:\Users\UIC\Desktop\FYP\vision_changing\iv\images.mp4 C:\Users\UIC\Desktop\FYP\color\DeOldify\video\source

REM Step 7: Run the Jupyter Notebook on deoldify
cd color/DeOldify
call conda activate deoldify
python videocolorizer.py
cd ..
cd ..

REM Step 8: color video to images
cd vision_changing\iv
copy C:\Users\UIC\Desktop\FYP\color\DeOldify\video\result\images.mp4 C:\Users\UIC\Desktop\FYP\vision_changing\iv
python vti.py images.mp4

REM step 9: transfer images to data's image
xcopy C:\Users\UIC\Desktop\FYP\vision_changing\iv\images_frames\* C:\Users\UIC\Desktop\FYP\gaussian3\gaussian-splatting-Windows\data\bat\images
cd ..
cd ..

REM step 10: train gaussian_splatting
cd gaussian3\gaussian-splatting-Windows
call conda activate gaussian_splatting
python train.py -s %4


REM step 11. view
./viewers/bin/SIBR_gaussianViewer_app -m %5

echo All steps completed.
pause
