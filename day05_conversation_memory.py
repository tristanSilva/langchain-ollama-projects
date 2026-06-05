from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3", temperature=0)

response_one = llm.invoke("My name is Tristan and I live in Naga City.")
print("Response: ", response_one.content)
print()

response_two = llm.invoke("What is my name and where do I live?")
print("Response: ", response_two.content)
print()
