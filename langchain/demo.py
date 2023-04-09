from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders.csv_loader import CSVLoader

loader = DirectoryLoader('./db', glob="**/*.csv", loader_cls=CSVLoader)

data = loader.load()

print(data[0])

print(data[0].metadata.update({"description": 'new!'}))

print(data[0])
