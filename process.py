# chroma client processes ingested data to vectors
import os
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    SentenceTransformersTokenTextSplitter,
)
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

seed_data = open("seed/all.txt", "r+")

character_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ". ", " ", ""], chunk_size=1000, chunk_overlap=0
)

character_split_texts = character_splitter.split_text("\n\n".join(seed_data))

token_splitter = SentenceTransformersTokenTextSplitter(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    chunk_overlap=0,
    tokens_per_chunk=256,
)

token_split_texts = []
for text in character_split_texts:
    token_split_texts += token_splitter.split_text(text)

embedding_function = SentenceTransformerEmbeddingFunction()

chroma_client = chromadb.PersistentClient() # saves to .chroma

chroma_collection = chroma_client.get_or_create_collection(
    "resume_data_01", embedding_function=embedding_function
)

ids = [str(i) for i in range(len(token_split_texts))]

chroma_collection.add(ids=ids, documents=token_split_texts)

print(chroma_collection)