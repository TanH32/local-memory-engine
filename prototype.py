memories = [
    "My name is Tanmay",
    "I am 5 foot 10 inches tall",
    "This is the first time I'm completely clueless",
    "Let's figure it out tho",
    "I am building a local chatbot memory search engine",
    "The deadline for the project is 10 October",
    "I'm trying to learn SQLite right now",
    "I have already used FastAPI before",
    "Let's see how this project goes",
]

def find_memories(query:str) -> list[str]:
    query = query.lower()


def main() -> None:
    query = input("Ask a question about the stored memories: ")
    matches = find_memories(query)
    if matches:
        print("Relevant memories:")
        for memory in matches:
            print(memory)
    else: 
        print("No relevant memory found")

if __name__ == "__main__":
    main()