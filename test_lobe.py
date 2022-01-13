from unet3d.inference.predict import predict
import os
import time

def get_nii(path):
    tmp_list = []
    for file in os.listdir(path):
        if os.path.splitext(file)[1] == '.gz':
            file_path = os.path.join(path, file)
            tmp_list.append(file_path)
    tmp_list.sort()
    return tmp_list


def segmentation(input_path, output_path):  # input_path文件路径与文件名，output_path保存路径，不需要有名
    model_path = './trained_models_lobe'
    _, fullflname = os.path.split(input_path)
    output_path = os.path.join(output_path, fullflname[:-7] + '.nii.gz')
    predict(model_path, input_path, output_path)


if __name__ == '__main__':
    time_start = time.time()
    input_path = r'F:\my_code\lobe_segmentation\test\lobe512.nii.gz'
    output_path = r'F:\my_code\lobe_segmentation\temp'
    segmentation(input_path, output_path)
    time_end = time.time()
    print(time_end - time_start)
