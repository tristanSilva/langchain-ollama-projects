from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

prompt = PromptTemplate(
  input_variables=["topic"],
  template="Explain {topic} in one sentence, like I am a Filipino Sofware Developer."
)

prompt2 = PromptTemplate(
  input_variables=["topic", "audience"],
  template="Explain {topic} in two sentences for {audience}"
)

formatted = prompt.format(topic="artificial intelligence")
print("formatted prompt: ")
print(formatted)
print()

formatted2 = prompt2.format(
  topic="LangChain",
  audience="a nestle business analyst in Naga City"
)

print("formatted2 prompt: ")
print(formatted2)
print()

response = llm.invoke(formatted)
print("LLM response: ")
print(response)

response2 = llm.invoke(formatted2)
print("LLM response 2: ")
print(response2)
