from PyPDF2 import PdfReader
from glob import glob
from os import path
from tqdm import tqdm

def extract(path):

    reader = PdfReader(path)
    text_complete = ""
    for page in reader.pages:
        text_complete += page.extract_text()
    return text_complete
    

def dir_search(dr):
    print('Building Corpus')
    p = path.join(dr,"*.pdf")
    res = glob(p)

    complete_text = ""
    for file_path in tqdm(res):
        try:
            complete_text += extract(file_path) + "\n"
        except:
            continue

    file1 = open("corpus.txt", "w")
    file1.write(complete_text)
    file1.close()

    return complete_text
    
def get_corpus():

    file1 = open("corpus.txt", "r")
    complete_text = file1.read()
    file1.close()

    return complete_text