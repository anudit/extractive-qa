from transformers import pipeline
from archive.extract import dir_search, get_corpus 

# https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation
# distilbert-base-cased-distilled-squad

qa_model = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

# corpus = dir_search('./schemes')
corpus = get_corpus()
print(len(corpus))

question = "List of assistive devices?"
res = qa_model(question = question, context = corpus)
print(res)
