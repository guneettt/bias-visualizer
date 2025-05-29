// Wait for the popup DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
  const selectedTextElement = document.getElementById("selected-text");
  const resultElement = document.getElementById("result");
  const analyzeBtn = document.getElementById("analyze-btn");

  // 🔹 1. Load highlighted text from Chrome storage
  chrome.storage.local.get(["selectedText"], (result) => {
    const text = result.selectedText;
    if (text && text.trim().length > 0) {
      selectedTextElement.textContent = text;
    } else {
      selectedTextElement.textContent = "No text selected.";
    }
  });

  // 🔹 2. Handle "Compare Bias" button click
  analyzeBtn.addEventListener("click", async () => {
    const keyword = selectedTextElement.textContent;

    if (!keyword || keyword === "No text selected.") {
      resultElement.innerHTML = `<p>Please highlight text before clicking.</p>`;
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ keyword })
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();

      resultElement.innerHTML = `
        <p><strong>Google Trends:</strong> ${data.google_interest}/100</p>
      `;
    } catch (err) {
      console.error("❌ Fetch error:", err);
      resultElement.innerHTML = `<p style="color:red;">Failed to get data. Is the API running?</p>`;
    }
  });
});
