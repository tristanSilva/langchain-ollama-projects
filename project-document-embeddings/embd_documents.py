import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

embedder = OllamaEmbeddings(model="nomic-embed-text")


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample_naga.txt")

loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=40)
chunks = splitter.split_documents(documents)

texts = [chunk.page_content for chunk in chunks]

all_vectors = embedder.embed_documents(texts)

print("Batch embeddings")

print(f"Number of chunks: {len(chunks)}")
print(f"Number of vectors: {len(all_vectors)}")
print(f"Dimension per vector: {len(all_vectors[0])}")
print()
