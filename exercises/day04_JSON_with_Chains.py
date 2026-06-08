from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3", temperature=0)
json_parser = JsonOutputParser()

json_prompt = PromptTemplate(
  template ="""You are a JSON API. Return only valid JSON. No explanation. No intro.

  start with {{ and end with }}.

  Return a JSON object with these keys:
  - term: the technology template_format
  - simple_definition: explain it like the person is a brangay captain
  - example: one real-world example in the Philippines

  Term to define: {term}""",
    input_variables=["term"]
)

json_chain = json_prompt | llm | json_parser
result = json_chain.invoke({"term": "Artifical Intelligence"})

print("Parsed JSON result:")
print(result)
print()
print("Simple definition:", result["simple definition"])
print("Philippine example:", result["example"])
