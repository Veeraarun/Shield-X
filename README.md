# Shield-X 🛡️

**Shield-X** is a lightweight web prototype for checking whether a URL appears in Google's Safe Browsing threat database. It was developed as a college hackathon project to explore practical web security and threat-intelligence workflows.

## ✨ Features

- URL input and validation at the UI level.
- FastAPI endpoint for URL analysis.
- Google Safe Browsing API integration.
- Checks for malware and social-engineering threats.
- Simple frontend risk-status display.
- Responsive, minimal interface.
- Demo screenshot and GIF included in the repository.

## 🏗️ Architecture

```text
Browser
   │
   │ GET /check_url/?url=...
   ▼
FastAPI Backend
   │
   │ threatMatches:find
   ▼
Google Safe Browsing API
   │
   ▼
Threat result
   │
   ▼
Browser UI
```

## 🛠️ Tech Stack

**Frontend**
- HTML5
- CSS3
- Vanilla JavaScript

**Backend**
- Python
- FastAPI
- Requests

**Security / Threat Intelligence**
- Google Safe Browsing API

## 📁 Project Structure

```text
Shield-X/
├── backend.py                 # FastAPI API
├── index.html                 # Frontend
├── script.js                  # API calls and result UI
├── style.css                  # Frontend styling
├── screenshot.png             # Demo screenshot
├── output-onlinegiftools.gif  # Demo animation
├── test.py                    # Basic test file
└── README.md
```

## 🚀 Local Setup

### 1. Clone

```bash
git clone https://github.com/Veeraarun/Shield-X.git
cd Shield-X
```

### 2. Install Python dependencies

```bash
pip install fastapi uvicorn requests
```

### 3. Configure the API key

The backend requires a Google Safe Browsing API key. Store it in an environment variable rather than committing a key to the repository.

For example:

```env
GOOGLE_API_KEY=your_api_key_here
```

Then update `backend.py` to read the value from the environment.

### 4. Start the API

```bash
uvicorn backend:app --reload --port 8000
```

The frontend currently expects the backend at `http://127.0.0.1:8000`.

## ⚠️ Security Note

**Do not commit API keys to GitHub.** If the key currently present in the repository is a real credential, revoke/rotate it and move the replacement to environment variables immediately.

## 🔍 How It Works

1. The user enters a URL.
2. The browser sends it to the FastAPI `/check_url/` endpoint.
3. FastAPI queries Google Safe Browsing for malware/social-engineering matches.
4. The backend returns whether matches were found.
5. The frontend displays the result.

## 📌 Project Status

Hackathon/educational prototype. It demonstrates the core URL threat-checking workflow but is not a complete production security product.

## 👥 Team

- Veeraarun V
- Vettrivelan G
- Ammu Krishnaprasad
- Roshni A

## 👤 Repository Owner

**Veeraarun V** — [GitHub](https://github.com/Veeraarun)
