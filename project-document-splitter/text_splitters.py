import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "Project_Apollo_Quantum_Computing.txt")

loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=40
)

chunks = splitter.split_documents(documents)

print("Document length (characters): ", len(documents[0].page_content))
print()
print(f"After splitting: {len(chunks)}")
print()

for inspect, chunk in enumerate(chunks):
    print(f"Chunk {inspect + 1} {len(chunk.page_content)} chars")
    print(chunk.page_content)
    print()

print("OVERLAPPING")

if len(chunks) >= 2:
    end_of_chunk1 = chunks[0].page_content[-40:]
    start_of_chunk2 = chunks[1].page_content[:40]

    print("Last 40 caharacters of chunk 1: ")
    print(repr(end_of_chunk1))
    print("First 40 characters of Chunk 2: ")
    print(repr(start_of_chunk2))
    print()

splitter_no_overlap = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)

chunks_no_overlap = splitter_no_overlap.split_documents(documents)

print("Without overlap")

for inspect, chunk in enumerate(chunks_no_overlap):
    print(f"Chunk {inspect + 1}")
    print(chunk.page_content)
    print()

print()
print("Chunk Comparison")
print()

for size in [100, 200, 500]:
    test_splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=int(size * 0.2)
    )

    test_chunk = test_splitter.split_documents(documents)
    print(f"Chunk size={size}, overlap={int(size * 0.2)} -> {len(test_chunk)}")
