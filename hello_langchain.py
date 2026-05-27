# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")
response = llm.invoke("what do you mean by orchestrate in LangChain?")
print(response)
