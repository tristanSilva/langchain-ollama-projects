# langchain-ollama-projects

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaLLM

langchain_core is the stable, maintained foundation. langchain_community is being phased out for many integrations.

model -> message -> invoke -> response
That is the atomic unit of every LangChain application.
