
import requests
from tqdm import tqdm
import json
from os import path

def load_json(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data

STORAGE_DIR = './downloaded'

def download_schemes():
    schemes = load_json('./secondlevel.json')
    for scheme in tqdm(schemes):
        ext_link = scheme[3].strip().lower()
        if ext_link.endswith('.pdf') or ext_link.endswith('.csv'):
            try:
                file_extension = ext_link.split('.')[-1]
                myfile = requests.get(ext_link, allow_redirects=True)
                if (myfile.status_code == 200):
                    open(path.join(STORAGE_DIR, scheme[0]+f'.{file_extension}'), 'wb').write(myfile.content)
            except:
                continue
            
download_schemes()