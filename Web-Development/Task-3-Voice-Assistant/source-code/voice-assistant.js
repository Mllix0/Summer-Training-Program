// ============================================================
// app.js — Voice assistant logic running in the browser
// ============================================================

const micBtn = document.getElementById("micBtn");
const micIcon = document.getElementById("micIcon");
const chatLog = document.getElementById("chatLog");
const statusText = document.getElementById("statusText");

// app.js and chat.php are located in the same project folder.
const BACKEND_URL = "./assistant.php";

// Language used for speech recognition and speech synthesis.
const LANG = "ar-SA";

let isListening = false;


// ------------------------------------------------------------
// Speech-to-Text setup
// ------------------------------------------------------------

const SpeechRecognitionAPI =
  window.SpeechRecognition || window.webkitSpeechRecognition;

if (!SpeechRecognitionAPI) {
  statusText.textContent =
    "متصفحك لا يدعم التعرف على الصوت. جرّب Chrome أو Edge.";

  micBtn.disabled = true;
} else {
  const recognition = new SpeechRecognitionAPI();

  recognition.lang = LANG;
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  micBtn.addEventListener("click", () => {
    if (isListening) {
      recognition.stop();
      return;
    }

    try {
      recognition.start();
    } catch (error) {
      console.error("تعذر بدء الاستماع:", error);

      statusText.textContent =
        "تعذر تشغيل الميكروفون. حاول مرة أخرى.";
    }
  });

  recognition.onstart = () => {
    isListening = true;

    micBtn.classList.add("listening");
    micIcon.textContent = "⏹️";

    statusText.textContent = "أستمع الآن... تحدّث بحرية";
  };

  recognition.onend = () => {
    isListening = false;

    micBtn.classList.remove("listening");
    micIcon.textContent = "🎤";

    statusText.textContent =
      "اضغط على الميكروفون وابدأ الحديث";
  };

  recognition.onerror = (event) => {
    console.error(
      "خطأ في التعرف على الصوت:",
      event.error
    );

    statusText.textContent =
      "لم أستطع سماعك، حاول مرة أخرى";
  };

  recognition.onresult = async (event) => {
    const userText =
      event.results[0][0].transcript.trim();

    if (!userText) {
      return;
    }

    addMessage("user", userText);

    const thinkingElement = addMessage(
      "bot",
      "...يفكر",
      { thinking: true }
    );

    try {
      const rawReply = await askGemini(userText);
      const cleanReply = cleanResponseText(rawReply);

      thinkingElement.remove();

      addMessage("bot", cleanReply);
      speak(cleanReply);
    } catch (error) {
      console.error(
        "Backend request failed:",
        error
      );

      thinkingElement.remove();

      addMessage(
        "bot",
        "حدث خطأ أثناء الاتصال بالخادم. حاول مجددًا."
      );
    }
  };
}


// ------------------------------------------------------------
// Backend communication
// ------------------------------------------------------------

async function askGemini(prompt) {
  const response = await fetch(BACKEND_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      prompt,
    }),
  });

  let data;

  try {
    data = await response.json();
  } catch (error) {
    throw new Error(
      "The server returned an invalid JSON response."
    );
  }

  if (!response.ok) {
    const serverMessage =
      data.error || `Server returned status ${response.status}.`;

    throw new Error(serverMessage);
  }

  if (
    typeof data.reply !== "string"
    || data.reply.trim() === ""
  ) {
    throw new Error(
      "The server returned an empty assistant response."
    );
  }

  return data.reply.trim();
}


// ------------------------------------------------------------
// Response text cleanup
// ------------------------------------------------------------

function cleanResponseText(text) {
  return text
    // Remove Markdown bold and italic markers.
    .replace(/\*\*(.*?)\*\*/g, "$1")
    .replace(/__(.*?)__/g, "$1")
    .replace(/\*(.*?)\*/g, "$1")
    .replace(/_(.*?)_/g, "$1")

    // Remove Markdown headings.
    .replace(/^#{1,6}\s+/gm, "")

    // Replace Markdown list markers with readable bullets.
    .replace(/^\s*[-*+]\s+/gm, "• ")

    // Remove inline-code markers.
    .replace(/`([^`]+)`/g, "$1")

    // Remove excessive empty lines.
    .replace(/\n{3,}/g, "\n\n")

    .trim();
}


// ------------------------------------------------------------
// Text-to-Speech
// ------------------------------------------------------------

function speak(text) {
  if (!("speechSynthesis" in window)) {
    return;
  }

  window.speechSynthesis.cancel();

  const utterance =
    new SpeechSynthesisUtterance(text);

  utterance.lang = LANG;
  utterance.rate = 1;

  window.speechSynthesis.speak(utterance);
}


// ------------------------------------------------------------
// Chat-interface utility
// ------------------------------------------------------------

function addMessage(role, text, options = {}) {
  const messageElement =
    document.createElement("div");

  messageElement.className =
    `message ${role}` +
    (options.thinking ? " thinking" : "");

  const paragraph =
    document.createElement("p");

  paragraph.textContent = text;

  messageElement.appendChild(paragraph);
  chatLog.appendChild(messageElement);

  chatLog.scrollTop = chatLog.scrollHeight;

  return messageElement;
}