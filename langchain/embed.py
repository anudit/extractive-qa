from dotenv import dotenv_values
config = dotenv_values('../.env')
print(config)

from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import DeepLake
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders.csv_loader import CSVLoader
import deeplake
from tqdm import tqdm


print('Loading directory')
loader = DirectoryLoader('./db', glob="**/*.csv", loader_cls=CSVLoader)
print('Loading data')
docs = loader.load()
print('found', len(docs), 'docs')


embeddings = HuggingFaceEmbeddings()


deeplake_path = 'hub://anudit/test_csv'

dl = DeepLake(dataset_path=deeplake_path, token=config['DEEPLAKE_API_TOKEN'], embedding_function=embeddings)

# db = dl.add_documents(docs);

retriever = dl.as_retriever()
retriever.search_kwargs['distance_metric'] = 'cos'
retriever.search_kwargs['fetch_k'] = 100
retriever.search_kwargs['maximal_marginal_relevance'] = True
retriever.search_kwargs['k'] = 20


hf_llm = HuggingFaceHub(
    repo_id="google/flan-t5-xl", 
    model_kwargs={"temperature":0, "max_length":64},
    huggingfacehub_api_token=config['HUGGINGFACEHUB_API_TOKEN']
)

from langchain.chains import ConversationalRetrievalChain

qa = ConversationalRetrievalChain.from_llm(hf_llm,retriever=retriever)

result = qa({"question": "which state in India has the largest population growth rate?", "chat_history": []})

print(result)