# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")
response = llm.invoke("In one sentence, what is LangChain?")
print(response)
