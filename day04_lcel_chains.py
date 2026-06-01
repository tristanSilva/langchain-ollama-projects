from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3", temperature=0)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
  ("system", "You are a helpful assitant. Answer in exactly one sentence."),
  ("human", "{question}")
])

chain = prompt | llm | parser

# For multiple Questions
questions = [
  "What is a vector dataabase?",
  "What is a RAG in AI?",
  "What is an AI agent?",
  "What is LangGraph?",
  "What is a prompt engineering?",
]

print("\nRunnin chain 5 times:\n")
for q in questions:
    result = chain.invoke({"question": q})
    print(f"Q: {q}")
    print(f"A: {result}")
    print()

# For Single Question
# response = chain.invoke({"question":"What is LangChain?"})

# print("Response:")
# print(response)
# print(type(response))
