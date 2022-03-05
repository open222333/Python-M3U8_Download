import os
import requests


def check_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_ts_list(m3u_path):
    '''讀取m3u8 取得ts檔'''
    with open(m3u_path, 'r') as f:
        context = f.readlines()

    result = []
    for i in context:
        if not i.startswith("#"):
            result.append(i.strip())
    return result


def is_m3u(file_name):
    '''是否為m3u檔'''
    target = ['.m3u', '.m3u8']
    ex = os.path.splitext(file_name)[1]
    return ex in target


def download_file(url, chunk_size=10240, dir=None):
    '''下載檔案'''
    local_filename = url.split('/')[-1]
    if dir != None:
        local_filename = f"{dir}/{local_filename}"
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    return local_filename
