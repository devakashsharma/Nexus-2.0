# import ollama

# def main():
#     print("You can start chatting with your LLaMA3 chatbot. Type 'exit' to quit.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'exit':
#             break

#         response = ollama.chat(
#             model='llama3',
#             messages=[
#                 {"role": "user", "content": user_input}
#             ]
#         )
#         print("Bot:", response['message']['content'])

# if __name__ == "__main__":
#     main()

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import json

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message")

    result = subprocess.run(
        ["ollama", "run", "llama3", user_input],
        capture_output=True,
        text=True
    )

    return {"response": result.stdout}
