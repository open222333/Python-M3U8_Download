from configparser import SafeConfigParser
import os


config = SafeConfigParser(os.environ)
config.read('config.ini')

SOURCE_DIR = config.get('M3U', 'SOURCE_DIR', fallback='m3u')
TARGET_URL = config.get('M3U', 'TARGET_URL', fallback=None)
TS_DIR = config.get('M3U', 'TS_DIR', fallback='ts')
