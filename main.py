from transformers import pipeline
from extract import dir_search 

# https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation
# distilbert-base-cased-distilled-squad

qa_model = pipeline("question-answering", model='deepset/deberta-v3-large-squad2')

corpus = dir_search('./schemes')

question = "List of assistive devices"


res = qa_model(question = question, context = corpus)
print(res)
