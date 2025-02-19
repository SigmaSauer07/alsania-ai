async function sendMessage() {
    let input = document.getElementById("userInput").value;
    let response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input_text: input })
    });
    let data = await response.json();
    document.getElementById("response").innerText = data.response;
}
