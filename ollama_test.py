import ollama
response = ollama.generate(model="llama3", prompt="hello")
print(response)