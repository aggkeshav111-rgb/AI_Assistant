# AI_Assistant_withFlask
# 🤖 AI Personal Assistant

A lightweight web application built with **Flask** and powered by the **OpenAI API** that lets you ask questions and summarize emails — all from a clean, responsive browser interface.

---

## ✨ Features

- **Ask Anything** — Chat with an AI personal assistant that answers any question in natural language.
- **Email Summarizer** — Paste a long email and get a concise 2–3 sentence summary instantly.
- **Async UI** — Responses are fetched without page reloads; a loading indicator keeps the UX smooth.

---

## 🗂️ Project Structure

```
AI_Assistant_withFlask/
│
├── main.py               # Flask app — routes and OpenAI API calls
├── .env                  # Your secret API key (not committed to Git)
├── .gitignore            # Ignores .env, __pycache__, etc.
│
├── templates/
│   └── index.html        # Frontend UI (HTML + vanilla JS)
│
└── static/
    └── style.css         # Styling for the web interface
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vivek30092/AI_Assistant_withFlask.git
cd AI_Assistant_withFlask
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask python-dotenv openai
```

### 4. Set Up Your OpenAI API Key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

### 5. Run the App

```bash
python main.py
```

Open your browser and navigate to **http://127.0.0.1:5000**

---

## 🔌 API Endpoints

| Method | Route        | Description                        |
|--------|--------------|------------------------------------|
| GET    | `/`          | Renders the main UI page           |
| POST   | `/ask`       | Accepts a question, returns an AI answer |
| POST   | `/summarize` | Accepts email text, returns a summary |

### Request / Response Format

Both `/ask` and `/summarize` accept `multipart/form-data` and return JSON:

**Request** (`/ask`)
```
question=What is the capital of France?
```

**Response**
```json
{
  "response": "The capital of France is Paris."
}
```

---

## 🛠️ Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Backend    | Python, Flask            |
| AI Engine  | OpenAI API (GPT model)   |
| Frontend   | HTML, Vanilla JS, CSS    |
| Config     | python-dotenv            |

---

## 📋 Requirements

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/account/api-keys)

---

## 🔒 Security Notes

- API keys are loaded from environment variables via `.env` — never hardcoded.
- The `.env` file is excluded from version control via `.gitignore`.

---
