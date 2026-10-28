# backend/main.py
from math import factorial

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pypinyin import lazy_pinyin, Style
from snownlp import SnowNLP
from datetime import datetime, timezone
import uuid
from fastapi import Request, Response

from storage import init_db, save_record, get_history  # ← 新增：跟存储层打交道，只经过这一行

init_db()  # ← 新增：启动时初始化数据库
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST"],
    allow_credentials=True,
)


profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
    "featuredWork": {
        "kicker": "作品",
        "title": "文字实验室",
        "copy": "拼音和情绪，挖掘中文里的细节",
        "linkLabel": "打开作品",
    },
    "identity": {
        "motto": "已识乾坤大，尤怜草木青",
        "learning": "零到全栈",
    },
}

class AnalyzeRequest(BaseModel):
    text: str

def get_session_id(request: Request, response: Response) -> str:
    sid = request.cookies.get("session_id")
    if not sid:
        sid = uuid.uuid4().hex
        response.set_cookie(
            "session_id", sid,
            httponly=True,
            samesite="lax",
            max_age=60 * 60 * 24 * 30,  # 30 天
        )
    return sid

def score_label(score):
    if score >= 0.6:
        return "偏积极"
    elif score <= 0.4:
        return "偏消极"
    else:
        return "中性"

@app.get("/api/profile")
def get_profile():
    return profile

@app.post("/api/analyze")
def analyze(req: AnalyzeRequest, request: Request, response: Response):
    sid = get_session_id(request, response)
    text = req.text
    score = round(SnowNLP(text).sentiments, 2)
    result = {
        "text": text,
        "score": score,
        "label": score_label(score),
        "pinyin": " ".join(lazy_pinyin(text, style=Style.TONE)),
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    save_record(sid, result)
    return result

@app.get("/api/history")
def history(request: Request, response: Response, limit: int = 10):
    sid = get_session_id(request, response)
    return get_history(sid, limit)
