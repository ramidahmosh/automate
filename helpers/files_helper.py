import os


def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except OSError:
        print("dir " + dir_path + " already exists")
    except:
        print("problem creating " + dir_path)


def create_multi_dirs(dir_path):
    try:
        os.makedirs(dir_path)
    except:
        print("problem creating  " + dir_path)
