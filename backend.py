from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Hardcoded Google API Key
GOOGLE_API_KEY = "AIzaSyCB6U3uGNcoLkAcMP3MPSQ2e0XcB-oJ6_M"  # Replace with your actual API key
SAFE_BROWSING_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

@app.get("/check_url/")
def check_url(url: str):
    payload = {
        "client": {"clientId": "threat-monitor", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }
    response = requests.post(f"{SAFE_BROWSING_URL}?key={GOOGLE_API_KEY}", json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="API Error")

    threats = response.json().get("matches", [])
    return {"url": url, "status": "unsafe" if threats else "safe"}
