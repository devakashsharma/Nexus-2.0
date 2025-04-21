async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const prompt = input.value;
    if (!prompt) return;
  
    chatBox.innerHTML += `<div><strong>You:</strong> ${prompt}</div>`;
    input.value = "";
  
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });
  
    const data = await response.json();
    chatBox.innerHTML += `<div><strong>Nexus:</strong> ${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  