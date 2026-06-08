from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

MODEL = "llama3"
TEMPERATURE = 0.7
SESSION_ID = "naga_session"

SYSTEM_PROMPT = """ You are NagaBot, a helpful local AI assistant running
entirely on a local machine in Naga City, Camarines Sur, Philippines.
You do not need the internet to work. You remember everything said
in this conversation. You answer clearly and concisely. When asked
about Naga City or Philippine topics, you are especially helpful."""

store ={}


def get_session_history(session_id: str) -> ChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# Chain Setup
llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

parser = StrOutputParser()

chain = prompt | llm | parser

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable": {"session_id": SESSION_ID}}


# Chat
def chat():
    print("=" * 60)
    print("NagaBot - Local AI Assistant")
    print("Powered by LangChain + Ollama + llama3")
    print("Running locally in Nagac City - no internet required")
    print("Type 'exit' or 'quit' to end convo")
    print("=" * 60)
    print()

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                print("NagaBot: Please type something\n")
                continue

            # What if it is empty
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("NagaBot: Goodbye! Conversation ended.")
                print(f"total turns: {len(store.get(SESSION_ID, ChatMessageHistory()).messages) //2}")
                break

            response = chain_with_memory.invoke(
                {"input": user_input},
                config=config
            )

            print(f"NagaBot: {response}")
            print()

        except KeyboardInterrupt:
            print("\nNagaBot: Session interrupted. Bye!")
            break
        except Exception as e:
            print(f"NagaBot: Something went wrong - {str(e)}")
            print("Please Try Again")


if __name__ == "__main__":
    chat()