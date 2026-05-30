from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm2 = OllamaLLM(model="llama3")

parser = JsonOutputParser()

prompt = PromptTemplate(
  template="""Answer the question below.

Return ONLY a valid JSON object. no explanation, no intro sentence, no markdown formatting.
Start your response with {{ and end with }}.

The JSON must have these exact keys:
- name: the technology name
- purpose: one sentence describing what it does
- used_for: a list of 3 use cases

Question: {question}""",
  input_variables=["question"]
)

formatted = prompt.format(question="What is LangChain?")
response = llm2.invoke(formatted)

print("Raw response:")
print(response)
print()

parsed = parser.invoke(response)
print("Parsed as Python dict:")
print(parsed)
print()
print("Accessing individual fields:")
print("Name:", parsed["name"])
print("Purpose:", parsed["purpose"])
print("Use cases:", parsed["used_for"])
