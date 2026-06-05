from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

llm = ChatOllama(model="llama3", temperature=0)
conversation_history = [
  SystemMessage(content="You are helpful assiatant who remembers everything said in this conversation.")
]

user_input = "My name is Tristan and I live in Naga City."
conversation_history.append(HumanMessage(content=user_input))

response = llm.invoke(conversation_history)
conversation_history.append(AIMessage(content=response.content))

print("Turn 1")
print("Human: ", user_input)
print("AI: ", response.content)
print()

user_input2 = "What is my name and where do I live?"
conversation_history.append(HumanMessage(content=user_input2))

response2 = llm.invoke(conversation_history)
conversation_history.append(AIMessage(content=response2.content))

print("Turn 2: ")
print("Human: ", user_input2)
print("AI: ", response2.content)
print()

user_input3 = "What is the nearest city to where I live?"
conversation_history.append(HumanMessage(content=user_input3))

response3 = llm.invoke(conversation_history)
conversation_history.append(AIMessage(content=response3.content))

print("Turn 3: ")
print("Human: ", user_input3)
print("AI: ", response3.content)
print()

print("Full conversation history sent to LLM on Turn 3: ")
for msg in conversation_history:
    print(f" {msg.type.upper()}: {msg.content[:80]}...")
