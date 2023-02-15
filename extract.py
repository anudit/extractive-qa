from PyPDF2 import PdfReader
from glob import glob
from os import path

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
    for file_path in res:
        complete_text += extract(file_path) + "\n"

    file1 = open("corpus.txt", "w")
    file1.write(complete_text)
    file1.close()

    return complete_text
    