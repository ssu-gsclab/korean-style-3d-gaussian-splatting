:: 1 = style_transfer (true 1, false 2)
:: 2 = input video name
:: 3 = gaussian step (min 100, max 30000)
:: 4 = object scale gaussian (true 1, false 2)

@echo off
:: init
SET style_Gaussian=C:\Users\tkdwn\Desktop\style_Gaussian
SET ouput_file_path=Z:\docker\gscServer\public\plyAssets\object

SET DATA_CHECK = %style_Gaussian%\input_video\%2.mp4

:: conda environment

:: ffmpeg

call python %style_Gaussian%\util\create_folder.py -i %style_Gaussian%\input_data -d 1
call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images\
call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images_lap\
call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images_dil\
call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images_trans\
call python %style_Gaussian%\util\remove.py -i %style_Gaussian%\styleTransfer\datasets\test\images_final\

call cd %style_Gaussian%\styleTransfer\datasets\test\images
call python %style_Gaussian%\util\ffmpeg.py -i %style_Gaussian%\input_video\%2.mp4 -f 4



:: style transfer gaussian
IF %1 EQU 1 (
	call python %style_Gaussian%\util\ffmpeg_vr.py -i %style_Gaussian%\styleTransfer\datasets\test\images
    call python %style_Gaussian%\util\laplacian.py
	copy %style_Gaussian%\styleTransfer\datasets\test\images\0001.png %style_Gaussian%\input_data\root\root.png > NUL

    :: style transfer 
	call cd %style_Gaussian%\styleTransfer
	conda activate sumuk_ST
	python test.py --dataroot %style_Gaussian%\styleTransfer\datasets\test\images_lap --num_test 10000 --name method_2 --save_path  %style_Gaussian%\styleTransfer\datasets\test\images_trans
	conda deactivate
    python test_convert.py 
    conda activate sumuk_ST
    :: python test.py --dataroot %style_Gaussian%\styleTransfer\datasets\test\images_dil --num_test 10000 --name Gyeomjae --save_path %style_Gaussian%\output_data\%5\input
    python test.py --dataroot %style_Gaussian%\styleTransfer\datasets\test\images_dil --num_test 10000 --name Gyeomjae --save_path %style_Gaussian%\styleTransfer\datasets\test\images_final
	conda deactivate
    python test_convert_2.py -i %style_Gaussian%\input_data\output\input
    :: style image resize process
	::call python %style_Gaussian%\util\pil.py -i %style_Gaussian%\input_data

    :: gaussian splatting
    call cd %style_Gaussian%\gaussian-splatting
    conda activate gaussian_splatting
    call python %style_Gaussian%\gaussian-splatting\convert.py -s %style_Gaussian%\input_data\output

    IF %4 EQU 1 call python %style_Gaussian%\util\transfer_png.py -i %style_Gaussian%\input_data/output/images

    call python %style_Gaussian%\gaussian-splatting\train.py -s %style_Gaussian%\input_data\output --iterations %3 --b %2 --resolution 4 --room_scale %4
    conda deactivate
    call python %style_Gaussian%\point-cloud-tools\convert.py %style_Gaussian%\output_list\%2.ply %2.splat --r %4

    call cd %style_Gaussian%
    
) ELSE IF %1 EQU 2 ( :: real world gaussian
    call python %style_Gaussian%\util\ffmpeg_vr.py -i %style_Gaussian%\styleTransfer\datasets\test\images
    call copy %style_Gaussian%\styleTransfer\datasets\test\images %style_Gaussian%\input_data\output\input
    :: gaussian splatting
    call cd %style_Gaussian%\gaussian-splatting
    conda activate gaussian_splatting
    call python %style_Gaussian%\gaussian-splatting\convert.py -s %style_Gaussian%\input_data\output

    IF %4 EQU 1 call python %style_Gaussian%\util\transfer_png.py -i %style_Gaussian%\input_data\output\images

    call python %style_Gaussian%\gaussian-splatting\train.py -s %style_Gaussian%\input_data\output --iterations %3 --b %2 --resolution 4 --room_scale %4
    conda deactivate
    call python %style_Gaussian%\point-cloud-tools\convert.py %style_Gaussian%\output_list\%2.ply %2.splat --r %4

    call cd %style_Gaussian%
)

:: gaussian retraining



