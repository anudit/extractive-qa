from dotenv import dotenv_values
config = dotenv_values('../.env')

from pprint import pprint
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

from langchain.vectorstores import DeepLake
deeplake_path = 'hub://anudit/test_csv'
db = DeepLake(dataset_path=deeplake_path, token=config['DEEPLAKE_API_TOKEN'], embedding_function=embeddings, read_only=True)
retriever = db.as_retriever()


query = 'Population Growth Rate of Uttar Pradesh?'
docs = db.similarity_search_with_score(query)

print('DeepLake')
pprint(docs)
print()

from langchain.chains import RetrievalQAWithSourcesChain
from langchain import HuggingFaceHub, PromptTemplate, OpenAI

template = """Question: {question}
    Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])

# --------
hf_llm = HuggingFaceHub(
    repo_id="google/flan-t5-xl", 
    model_kwargs={"temperature":0.1, "max_length":200},
    huggingfacehub_api_token=config['HUGGINGFACEHUB_API_TOKEN']
)

chain = RetrievalQAWithSourcesChain.from_chain_type(hf_llm, chain_type="stuff", retriever=retriever, verbose=True)


print(f'HF LLM: google/flan-t5-xl')
docs_hf = chain({"question": query}, return_only_outputs=True)
pprint(docs_hf)
print()

# --------

from langchain.chat_models import ChatOpenAI

openai_llm = ChatOpenAI(openai_api_key=config['OPENAI_API_TOKEN'])

chain = RetrievalQAWithSourcesChain.from_chain_type(openai_llm, chain_type="stuff", retriever=retriever, verbose=True)
print(f'OpenAI gpt-3.5-turbo LLM')
docs_hf = chain({"question": query}, return_only_outputs=True)
pprint(docs_hf)
print()