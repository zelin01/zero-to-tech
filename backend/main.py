from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from pypinyin import lazy_pinyin, Style
from snownlp import SnowNLP

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
    }