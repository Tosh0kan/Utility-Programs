import os
import shutil

def clear_cache():
    appdata = os.getenv('APPDATA')
    shutil.rmtree(appdata + r'\discord\Cache')

if __name__ == '__main__':
    clear_cache()
