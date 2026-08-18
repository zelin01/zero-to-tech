"use client";

// 文字实验室的"输入区"卡片。和 4.4 一字未改。
// text 是这张卡自己揣着的 state，打字就变、下面"已输入 N 字"当场跟着跳。
// 因为用了 useState，要在浏览器里跑，所以顶上标了 "use client"。
import { useState } from "react";

export default function InputCard({ onResult}) {
  const [text, setText] = useState("今天的风很轻，适合把脑海里的想法慢慢写下来。");
  const [error, setError] = useState("");

  async function handleAnalyze() {
    setError("");

    try {
      const res = await fetch("http://localhost:8000/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.detail || `分析失败：${res.status}`);
      }

      onResult(await res.json());
    } catch (error) {
      setError(error.message);
    }
  }

  return (
    <article className="panel panel-half lab-panel card">
      <div className="panel-heading">
        <p className="section-kicker">输入区</p>
        <h3>贴一段中文</h3>
      </div>
      <form className="lab-form" onSubmit={(e) => e.preventDefault()}>
        <label htmlFor="text-input">文本内容</label>
        <textarea
          id="text-input"
          rows="8"
          placeholder="例如：生活没有标准答案，但每一天都值得认真感受。"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        {/* state 现身：text 一变，这行数字自动跟着变 */}
        <p className="lab-count">已输入 {text.length} 字</p>
        {error && <p className="lab-error">{error}</p>}
        <button className="primary-button" type="button" onClick={handleAnalyze}>开始分析</button>
      </form>
    </article>
  );
}
