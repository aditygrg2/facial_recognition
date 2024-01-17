import os

def get_lfw(lfw_folder_path):
    for folders in os.listdir(lfw_folder_path):
        for files in os.listdir(os.path.join(lfw_folder_path, folders)):
            os.rename(os.path.join(lfw_folder_path,folders, files), 'negative_img_train/' + files)

get_lfw()

## Enter the path in the function above