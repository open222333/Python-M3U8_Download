from general.function import get_ts_list, is_m3u, download_file, check_dir
from general import TARGET_URL, TS_DIR, SOURCE_DIR
import os

check_dir(SOURCE_DIR)
check_dir(TS_DIR)

all_files = os.listdir(SOURCE_DIR)
for file in all_files:
    if is_m3u(file):
        for ts in get_ts_list(f'{SOURCE_DIR}/{file}'):
            url = f"{TARGET_URL}/{ts}"
            download_file(url, dir=TS_DIR)
