from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3", temperature=0)

prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a senior software engineer whose patient in answers."),
  ("human", "{question}")
])

parser = StrOutputParser()

messages = prompt.format_messages(question="What is underneath langchain?")
response = llm.invoke(messages)

print("Without parser: ")
print(response)
print()

parsed = parser.invoke(response)
print("With parser:")
print(parsed)
print()
