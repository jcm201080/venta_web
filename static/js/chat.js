document.addEventListener("DOMContentLoaded", () => {

const toggle = document.getElementById("chat-toggle");
const chatbot = document.getElementById("chatbot");
const input = document.getElementById("chat-input");
const body = document.getElementById("chat-body");
const closeBtn = document.getElementById("chat-close");

let timeout;

function addMessage(text, type) {
    const msg = document.createElement("div");
    msg.classList.add("msg", type);
    msg.innerHTML = text;
    body.appendChild(msg);
    body.scrollTop = body.scrollHeight;
}

function resetTimeout() {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        chatbot.classList.add("hidden");
    }, 30000);
}

toggle.onclick = () => {
    chatbot.classList.toggle("hidden");
    input.focus();
    resetTimeout();
};

closeBtn.onclick = () => {
    chatbot.classList.add("hidden");
    clearTimeout(timeout);
};

input.addEventListener("input", () => {
    clearTimeout(timeout);
});

input.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        e.preventDefault();

        let msg = input.value.trim();
        if (!msg) return;

        addMessage(msg, "user");

        fetch("/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({mensaje: msg})
        })
        .then(res => res.json())
        .then(data => {
            addMessage(data.respuesta.replace(/\n/g, "<br>"), "bot");
        })
        .catch(err => {
            addMessage("Error conectando con la IA", "bot");
            console.error(err);
        });

        input.value = "";
        resetTimeout();
    }
});

});