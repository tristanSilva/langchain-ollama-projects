from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

chat_llm = ChatOllama(model="llama3")

chat_prompt = ChatPromptTemplate.from_messages([
  ("system", "you are a helpful assistant who always answers in simple Filipino English."),
  ("human", "what is {concept} and why does it matter?")
])

messages = chat_prompt.format_messages(concept="RAG - Retrieval Augmented Generation")

print("Chat messages:")

for msg in messages:
    print(f"{msg.type.upper()}: {msg.content}")
print()

response3 = chat_llm.invoke(messages)
print("Chat response:")
print(response3.content)
