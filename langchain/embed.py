import os
from dotenv import load_dotenv

load_dotenv('../.env')
os.environ['NUMEXPR_MAX_THREADS'] = str(os.cpu_count())
os.environ['NUMEXPR_NUM_THREADS'] = str(os.cpu_count())

import logging
logging.basicConfig(level=logging.DEBUG)

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import DeepLake
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import PyPDFLoader
from tqdm import tqdm
from langchain.vectorstores import FAISS

def run_stuff():

    print('Loading directory')
    # loader = DirectoryLoader('../census/census_csvs', glob="**/PC11_*.csv", loader_cls=CSVLoader, show_progress=True)
    loader = DirectoryLoader('../mospi/downloaded', glob="**/*.pdf", loader_cls=PyPDFLoader, show_progress=True, silent_errors=True)
    print('Loading data')
    docs = loader.load()
    print('found', len(docs), 'docs')

    print('Optimizing Metadata')
    for ind in tqdm(range(0, len(docs))):
        docs[ind].metadata['source'] = docs[ind].metadata['source'].replace(('../mospi/downloaded/'),'')

    embeddings = HuggingFaceEmbeddings()

    db = FAISS.from_documents(docs, embeddings)
    db.save_local("./mospi_faiss_index")

    # deeplake_path = 'hub://anudit/test_csv'
    # dl = DeepLake(
    #     dataset_path=deeplake_path, 
    #     token=os.environ['DEEPLAKE_API_TOKEN'], 
    #     embedding_function=embeddings
    # )

    # dl.add_documents(docs)

if __name__ == '__main__':
    run_stuff()