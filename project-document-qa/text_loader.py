import os
from langchain_community.document_loaders import TextLoader

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample_naga.txt")

loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

print("Number of documents: ", len(documents))
print("Type of first documents: ", type(documents[0]))
print("Page content: ")
print(documents[0].page_content)
print()
print("Metadata: ")
print(documents[0].metadata)

doc = documents[0]

print("Characters length: ", len(doc.page_content))
print("Words length: ", len(doc.page_content.split()))
print("First 100 character: ")
print(doc.page_content[:100])
print("Last 100 characters: ")
print(doc.page_content[-100:])
print("Source : ", doc.metadata.get("source"))
print()
