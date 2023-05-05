
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
    schemes = load_json('./firstlevel.json')
    for row in tqdm(schemes):
        title = row[0]
        ext_link = row[1]
        if ext_link.endswith('.pdf'):
            try:
                myfile = requests.get(ext_link, allow_redirects=True, timeout=10)
                if (myfile.status_code == 200):
                    open(path.join(STORAGE_DIR, f'{title}.pdf'), 'wb').write(myfile.content)
            except:
                continue
            
download_schemes()