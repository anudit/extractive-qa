
import requests
from tqdm import tqdm
import json
from os import path

def load_json(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data

STORAGE_DIR = './schemes'

def download_schemes():
    schemes = load_json('./secondlevel.json')
    for scheme in tqdm(schemes):
        ext_link = scheme[3].strip()
        if ext_link.endswith('.pdf'):
            try:
                myfile = requests.get(ext_link, allow_redirects=True)
                if (myfile.status_code == 200):
                    open(path.join(STORAGE_DIR, scheme[0]+'.pdf'), 'wb').write(myfile.content)
            except:
                continue
            
download_schemes()