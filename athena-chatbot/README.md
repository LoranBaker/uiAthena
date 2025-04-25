# Athena AI – Demo Chatbot Interface

This is a simple Athena Chatbot demo using Streamlit as the frontend and Athena FastAPI as the backend. It allows users to chat with Athena AI, and stores session-based message history. Use for demos only, quickly developed to serve for showcase purposes.

## Prerequisites

- Python 3.8+
- `pip` (Python package manager)
- A working internet connection (for API calls or ngrok tunneling if shared)
- `ngrok` (optional – for sharing the app externally)

---

## Installation

1. **Clone the repo** (if not already done):

```bash
git clone [repo-link]
cd athena-chatbot
```

2. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, manually install:

```bash
pip install streamlit fastapi pydantic uvicorn requests
```

---

## Project Structure

```
athena-chatbot/
│
├── main.py             # Streamlit frontend (UI and chat logic)
├── logo.png            # Envalpro logo
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── Run app.bat         # Windows batch script to run the app
├── venv/               # Python virtual environment (optional)
└── .streamlit/
    └── config.toml     # Streamlit UI config – customize fonts, colors, etc.
```

---

## Running the App Locally

1. **Start the FastAPI Athena backend**.

2. **In another terminal, run the Streamlit app**:

```bash
python -m streamlit run main.py
```

3. Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## (Optional) Expose Public Link via Ngrok

To allow external users (e.g., testers or friends) to access the app:

```bash
ngrok http 8501
```

Copy the public forwarding URL (e.g., `https://abcd1234.ngrok.io`) and share it.

> The FastAPI backend **does not need to be exposed** if it's running on the same machine – Streamlit calls it locally.

---

## Chat Flow (Simplified)

1. User enters a message.
2. Streamlit sends the input + session ID to FastAPI Athena backend.
3. FastAPI returns a response.
4. Response is displayed, and the chat history is updated.

---

## Maintainer

Project handed over by Solarise team, continued by Loran Baker.