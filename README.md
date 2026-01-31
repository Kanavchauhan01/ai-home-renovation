# 🏡 AI Home Renovation Assistant

An AI-powered web application that helps users plan home renovations based on their **budget and requirements**.  
Built using **Google Gemini AI** and **Streamlit**, and deployed live on **Streamlit Cloud**.

🔗 **Live App:**  
https://ai-home-renovation-kanavchauhan.streamlit.app/

---

## 🚀 Features

- 💡 AI-generated home renovation suggestions
- 💰 Budget-based planning (e.g. kitchen renovation under ₹20,000)
- 🧠 Powered by Google Gemini (text-based AI)
- 🌐 Deployed online for free using Streamlit Cloud
- 🔐 Secure API key handling using environment secrets

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **GitHub**
- **Streamlit Cloud**

---

## 📂 Project Structure

# 🏡 AI Home Renovation Assistant

An AI-powered web application that helps users plan home renovations based on their **budget and requirements**.  
Built using **Google Gemini AI** and **Streamlit**, and deployed live on **Streamlit Cloud**.

🔗 **Live App:**  
https://ai-home-renovation-kanavchauhan.streamlit.app/

---

## 🚀 Features

- 💡 AI-generated home renovation suggestions
- 💰 Budget-based planning (e.g. kitchen renovation under ₹20,000)
- 🧠 Powered by Google Gemini (text-based AI)
- 🌐 Deployed online for free using Streamlit Cloud
- 🔐 Secure API key handling using environment secrets

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **GitHub**
- **Streamlit Cloud**

---

## 📂 Project Structure

ai-home-renovation/
│
├── streamlit_app.py # Main Streamlit application
├── requirements.txt # Project dependencies
└── README.md # Project documentation

## ⚙️ How It Works

1. User enters renovation requirements (e.g. room type & budget)
2. The input is sent to Google Gemini AI
3. AI generates a detailed renovation plan
4. Output is displayed instantly in the web app

---

## 🔑 API Key Setup (For Local Run)

This project uses **Google Gemini API**.

### 1. Get API Key
- Visit Google AI Studio
- Generate a Gemini API key

### 2. Add API Key (Local)
Create an environment variable:

```bash
GOOGLE_API_KEY=your_api_key_here

 3. Add API Key (Streamlit Cloud)
In Advanced Settings → Secrets:

GOOGLE_API_KEY = "your_api_key_here"
