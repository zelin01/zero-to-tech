import { useEffect, useRef } from "react";
import { animate, scrambleText } from "animejs";

export default function ResultCard () {
    const cardRef = useRef(null);
    const scoreRef = useRef(null);

    useEffect(() => {
        animate(cardRef.current, {
            opacity: [0, 1],
            translateY: [24, 0],
            duration: 700,
            ease: "outBack",
        });
        animate(scoreRef.current, {
            innerHTML: scrambleText({ chars: "0-9" }),
            duration: 1500,
        });
    }, []);

    return (
        <article ref={cardRef} className="panel panel-half result-panel card">
            <div className="panel-heading">
                <p className="section-kicker">结果区</p>
                <h3>分析结果</h3>
            </div>
            <div className="result-stack">
                <div className="result-item">
                    <span>原文</span>
                    <p>今天的月色很美</p>
                </div>
                <div className="result-item">
                    <span>拼音</span>
                    <p>jīn tiān de yuè sè hěn měi</p>
                </div>
                <div className="result-grid">
                    <div className="result-badge">
                        <span>情感分数</span>
                        <strong data-score ref={scoreRef}>0.86</strong>
                    </div>
                    <div className="result-badge">
                        <span>情感判断</span>
                        <strong>偏积极</strong>
                    </div>
                </div>
            </div>
        </article>
    );
};