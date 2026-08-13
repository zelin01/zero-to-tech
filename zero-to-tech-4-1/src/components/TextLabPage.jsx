import Nav from "./Nav.jsx";
import PageHeading from "./PageHeading.jsx";
import AnimatedCardGrid from "./AnimatedCaridGrid.jsx";
import InputCard from "./InputCard.jsx";
import ResultCard from "./ResultCard.jsx";
import React from "react";

export default function TextLabPage({ current, onNavigate}) {
    return (
        <AnimatedCardGrid className="dashboard-grid">
            <article className="hero-stage panel-full">
                <Nav current={current} onNavigate={onNavigate} />
                <PageHeading title="文本实验室" description="在这里，你可以输入一段文本，系统将为你分析其情感倾向。" />
            </article>

            <InputCard />
            <ResultCard />
        </AnimatedCardGrid>
    );
}