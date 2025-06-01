document.addEventListener("DOMContentLoaded", () => {
  const selectedTextElement = document.getElementById("selected-text");
  const analyzeBtn = document.getElementById("analyze-btn");
  const page1 = document.getElementById("page1");
  const page2 = document.getElementById("page2");
  const trendScore = document.getElementById("trend-score");

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
      alert("Please highlight text before clicking Compare Bias.");
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

      // ✅ Show trend score
      trendScore.textContent = `${data.google_interest}/100`;

      // ✅ Render chart
      if (data.timeline && Array.isArray(data.timeline)) {
        console.log("🧪 Timeline data:", data.timeline);
        renderBarChart(data.timeline);
      }

    } catch (err) {
      console.error("❌ Fetch error:", err);
      alert("Failed to get data. Is the API running?");
    }
  });
});

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
        backgroundColor: "rgba(29, 191, 115, 0.85)",
        borderRadius: 6,
        barThickness: 24,
        borderSkipped: false
      }]
    },
    options: {
      responsive: true,
      animation: {
        duration: 700,
        easing: 'easeOutQuart'
      },
      layout: {
        padding: {
          top: 2,
          bottom: 0 // ⬅️ removed bottom space
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: "Search Popularity",
            align: "center",
            color: "#ffffff",
            font: {
              family: "Poppins, sans-serif",
              size: 9,
              weight: "600"
            },
            padding: { bottom: 2 }
          },
          grid: {
            color: "#333",
            borderColor: "#ffffff" // ✅ White Y axis line
          },
          ticks: {
            color: "#ffffff",
            font: {
              family: "Poppins, sans-serif",
              size: 8,
              weight: "400"
            }
          }
        },
        x: {
          title: {
            display: true,
            text: "Date",
            align: "center", // ✅ Centered title
            color: "#ffffff",
            font: {
              family: "Poppins, sans-serif",
              size: 9,
              weight: "600"
            },
            padding: { top: 2 }
          },
          grid: {
            display: false,
            borderColor: "#ffffff" // ✅ White X axis line
          },
          ticks: {
            color: "#ffffff",
            font: {
              family: "Poppins, sans-serif",
              size: 8,
              weight: "400"
            },
            maxRotation: 30,
            minRotation: 30
          }
        }
      },
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          backgroundColor: "#2b2b2b",
          titleColor: "#fff",
          bodyColor: "#1dbf73",
          borderColor: "#1dbf73",
          borderWidth: 1
        }
      }
    }
  });
}