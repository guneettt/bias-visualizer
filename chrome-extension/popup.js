document.addEventListener("DOMContentLoaded", () => {
  const selectedTextElement = document.getElementById("selected-text");
  const resultElement = document.getElementById("result");
  const analyzeBtn = document.getElementById("analyze-btn");
  const page1 = document.getElementById("page1");
  const page2 = document.getElementById("page2");

  // 🔹 Load highlighted text from Chrome storage
  chrome.storage.local.get(["selectedText"], (result) => {
    const text = result.selectedText;
    if (text && text.trim().length > 0) {
      selectedTextElement.textContent = text;
    } else {
      selectedTextElement.textContent = "No text selected.";
    }
  });

  // 🔹 Handle "Compare Bias" button click
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

      // ✅ Switch to Page 2
      page1.classList.remove("active");
      page2.classList.add("active");

      // ✅ Render Results
      resultElement.innerHTML = `
        <p><strong>Google Trends:</strong> ${data.google_interest}/100</p>
      `;

      // ✅ Render Bar Chart
      if (data.timeline && Array.isArray(data.timeline)) {
        console.log("🧪 Timeline data:", data.timeline);
        renderBarChart(data.timeline);
      }

    } catch (err) {
      console.error("❌ Fetch error:", err);
      resultElement.innerHTML = `<p style="color:red;">Failed to get data. Is the API running?</p>`;
    }
  });
});

// 🔹 Chart rendering function
function renderBarChart(data) {
  const ctx = document.getElementById("trendsChart").getContext("2d");

  if (window.trendsChartInstance) {
    window.trendsChartInstance.destroy();
  }

  window.trendsChartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: data.map(point => point.time),
      datasets: [{
        label: "Search Interest (Past 7 Days)",
        data: data.map(point => point.value),
        backgroundColor: "rgb(212, 212, 212)",
        borderColor: "rgb(244, 244, 244)",
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      },
      plugins: {
        legend: { display: false }
      }
    }
  });
}