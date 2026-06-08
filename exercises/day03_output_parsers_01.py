from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

prompt = ChatPromptTemplate.from_messages([
  ("system", "You are concise assitant"),
  ("human", "{question}")
])

parser = StrOutputParser()

messages = prompt.format_messages(question="What is Python in one sentence?")
response = llm.invoke(messages)

print("Without parser")
print(response)
print()

parsed = parser.invoke(response)
print("With parser")
print(parsed)
print(type(parsed))
