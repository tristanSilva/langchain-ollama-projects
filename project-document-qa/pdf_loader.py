import os
from langchain_community.document_loaders import PyPDFLoader

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample-local-pdf.pdf")

print(file_path)

pdf_loader = PyPDFLoader(file_path)
pdf_documents = pdf_loader.load()

print()
print("Number of pages : ", len(pdf_documents))
print()

for inspect, page in enumerate(pdf_documents):
    print(f"Page {inspect + 1}: ")
    print(f"Characters: {len(page.page_content)}")
    print(f"Words : {len(page.page_content.split())}")
    print(f"Metadata: {page.metadata}")
    print(f" first 10 characters: {page.page_content[:10]}")
    print()
