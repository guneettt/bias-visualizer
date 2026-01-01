# 🧠 Bias Visualizer - Chrome Extension + API

Bias Visualizer is a lightweight Chrome extension that allows users to highlight any text on a webpage and instantly compare its popularity across **Google Trends** (real-world interest) vs curated platforms. It's a fast, intuitive way to visualize how topics trend online - and where media attention might diverge from public interest.

This is a **portfolio project** designed to demonstrate real-world API integration, frontend-backend communication, and full-stack product thinking.

---

## 📌 Description  
**A Chrome Extension + FastAPI web app to visualize real-world interest (Google Trends) vs curated timelines - highlighting digital media bias in trending topics. Built for my portfolio.**

---

## 🎯 Features

- ✅ **Highlight any text** on a webpage  
- 📊 **Compare real-world vs media interest** using Google Trends  
- ⚡ **FastAPI backend** for seamless data processing  
- 📈 Dynamic chart rendering with **Chart.js**  
- 🎯 Built as a **Chrome Extension** using Manifest v3  
- 🧠 Real-time keyword analysis with daily trend breakdown  

---

## 🛠️ Tech Stack

| Frontend              | Backend           | Tools & APIs       |
|-----------------------|--------------------|---------------------|
| HTML + JS + Chart.js  | FastAPI (Python)   | Google Trends API   |
| Chrome Extensions     | CORS Middleware    | Pydantic            |
| Content Scripts       | REST API           |                     |

---

## 🖼️ Demo

> Highlight any text → Click “Compare Bias” → View the Google Trends chart

![Demo](demo.gif)

---

## 🚀 Getting Started

### 🧩 1. Load the Chrome Extension

1. Clone this repository
2. Open Chrome and go to `chrome://extensions`
3. Enable “Developer Mode” (top-right)
4. Click “Load unpacked” and select the `chrome-extension/` folder

### 🔌 2. Start the Backend Server

```bash
# From project root
uvicorn main:app --reload
