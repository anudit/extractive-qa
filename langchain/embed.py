import os
from dotenv import load_dotenv

load_dotenv('../.env')
os.environ['NUMEXPR_MAX_THREADS'] = '12'
os.environ['NUMEXPR_NUM_THREADS'] = '12'

import logging
logging.basicConfig(level=logging.DEBUG)

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import DeepLake
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders.csv_loader import CSVLoader
from tqdm import tqdm
from langchain.vectorstores import FAISS

print('Loading directory')
loader = DirectoryLoader('../census/census_csvs', glob="**/1991-B02T-*.csv", loader_cls=CSVLoader)
print('Loading data')
docs = loader.load()
print('found', len(docs), 'docs')

embeddings = HuggingFaceEmbeddings()

db = FAISS.from_documents(docs, embeddings)
db.save_local("./faiss_index")

# deeplake_path = 'hub://anudit/test_csv'
# dl = DeepLake(
#     dataset_path=deeplake_path, 
#     token=os.environ['DEEPLAKE_API_TOKEN'], 
#     embedding_function=embeddings
# )

# dl.add_documents(docs)