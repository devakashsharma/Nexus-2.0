from ollama import Client # type: ignore

client = Client(host='http://localhost:11434')  # default Ollama server

print("You can start chatting with LLaMA3! Type 'exit' to quit.")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break

    response = client.chat(
        model='llama3',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("Bot:", response['message']['content'])