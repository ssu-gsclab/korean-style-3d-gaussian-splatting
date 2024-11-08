:: 1 = style_transfer (true 1, false 2)
:: 2 = VR VIDEO (true 1, false 2) delete
:: 3 = ffmpeg frame num (min 1, max 10) delete
:: 4 = gaussian step (min 100, max 30000)
:: 5 = input video name
:: 6 = object scale gaussian (true 1, false 2)

@echo off

:: init
SET style_Gaussian="C:\Users\tkdwn\Desktop\style_Gaussian"

:: conda environment
:: call C:\Users\tkdwn\anaconda3\Scripts/activate.bat C:\Users\tkdwn\anaconda3

:: ffmpeg
IF %1 NEQ 3 (
    call python %style_Gaussian%\util\create_folder.py -i %style_Gaussian%\output_data\%5 -d 1
    :: d is last file delete before create_folder true = 1, false = 2 / run_group file don't need delete method 
    call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images\
    call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images_lap\
    call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images_dil\
    call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images_trans\
    call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images_final\
    call cd %style_Gaussian%\styleTransfer\datasets\test\images
    ::ffmpeg -i %style_Gaussian%\input_video\%5.mp4 -qscale:v 1 -qmin 1 -vf fps=2 %%04d.png
    call python %style_Gaussian%\util\ffmpeg.py -i %style_Gaussian%\input_video\%5 -f %3
    call python %style_Gaussian%\util\laplacian.py
)

:: style transfer gaussian
IF %1 EQU 1 (
	IF %2 EQU 1 call python %style_Gaussian%\util\ffmpeg_vr.py -i %style_Gaussian%\styleTransfer\datasets\test\images
	call copy %style_Gaussian%\styleTransfer\datasets\test\images\0001.png %style_Gaussian%\output_data\%5\root\root.png

    :: style transfer 
	call cd %style_Gaussian%\styleTransfer
	conda activate sumuk_ST
	python test.py --dataroot %style_Gaussian%\styleTransfer\datasets\test\images_lap --num_test 10000 --name method_1 --save_path  %style_Gaussian%\styleTransfer\datasets\test\images_trans
	conda deactivate
    python test_convert.py 
    conda activate sumuk_ST
    :: python test.py --dataroot %style_Gaussian%\styleTransfer\datasets\test\images_dil --num_test 10000 --name Gyeomjae --save_path %style_Gaussian%\output_data\%5\input
    python test.py --dataroot %style_Gaussian%\styleTransfer\datasets\test\images_dil --num_test 10000 --name Gyeomjae --save_path %style_Gaussian%\styleTransfer\datasets\test\images_final
	conda deactivate
    python test_convert_2.py -i %style_Gaussian%\output_data\%5\input


    :: style image resize process
	call python %style_Gaussian%\util\pil.py -i %style_Gaussian%\output_data\%5

    :: gaussian splatting
    call cd %style_Gaussian%\gaussian-splatting
    conda activate gaussian_splatting
    call python %style_Gaussian%\gaussian-splatting\convert.py -s %style_Gaussian%\output_data\%5\output
    
    IF %6 EQU 1 call python %style_Gaussian%\util\transfer_png.py -i %style_Gaussian%\output_data\%5\output\images
    
    call python %style_Gaussian%\gaussian-splatting\train.py -s %style_Gaussian%\output_data\%5\output --iterations %4 --b %5 --resolution 1 --room_scale %6
    conda deactivate

    call cd %style_Gaussian%
) 

:: real world gaussian
IF %1 EQU 2 (
    IF %2 EQU 1 call python %style_Gaussian%\util\ffmpeg_vr.py -i %style_Gaussian%\styleTransfer\datasets\test\images

    call copy %style_Gaussian%\styleTransfer\datasets\test\images %style_Gaussian%\output_data\%5\output\input
    ::call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images
    :: gaussian splatting
    call cd %style_Gaussian%\gaussian-splatting
    conda activate gaussian_splatting
    call python %style_Gaussian%\gaussian-splatting\convert.py -s %style_Gaussian%\output_data\%5\output
    
    IF %6 EQU 1 call python %style_Gaussian%\util\transfer_png.py -i %style_Gaussian%\output_data\%5\output\images

    call python %style_Gaussian%\gaussian-splatting\train.py -s %style_Gaussian%\output_data\%5\output --iterations %4 --b %5 --resolution 1 --room_scale %6
    conda deactivate
    call cd %style_Gaussian%
)

:: gaussian retraining
IF %1 EQU 3 (
    ::IF %6 EQU 1 call python %style_Gaussian%\util\transfer_png.py -i %style_Gaussian%\output_data\%5\output\images
    :: gaussian splatting
    call cd %style_Gaussian%\gaussian-splatting
    conda activate gaussian_splatting
    call python %style_Gaussian%\gaussian-splatting\train.py -s %style_Gaussian%\output_data\%5\output --iterations %4 --b %5 --resolution 1 --room_scale %6
    conda deactivate
    call cd %style_Gaussian%
)
