from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from pypinyin import lazy_pinyin, Style
from snownlp import SnowNLP
import json
from datetime import datetime, timezone
import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"]
)

class AnalyzeRequest(BaseModel):
    text: str

def text_label(score):
    if score >= 0.6:
        return "偏积极"
    elif score <= 0.4:
        return "偏消极"
    return "中性"

def load_history():
    try:
        with open("./history/history.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_history(history):
    records = load_history()
    records.append(history)
    with open("./history/history.json", "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

@app.get("/api/profile")
def get_profile():
    return

@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    text = req.text
    score = round(SnowNLP(text).sentiments, 2)
    return {
        "text": text,
        "score": score,
        "label": text_label(score),
        "pinyin": "".join(lazy_pinyin(text, style=Style.TONE)),
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    save_record(result)
    return result

@app.get("/api/history")
def history():
    records = load_history()
    records.reverse()
    return records[:10]