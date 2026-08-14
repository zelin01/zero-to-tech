import Nav from "./Nav.jsx";
import PageHeading from "./PageHeading.jsx";
import AnimatedCardGrid from "./AnimatedCaridGrid.jsx";
import InputCard from "./InputCard.jsx";
import ResultCard from "./ResultCard.jsx";
import { textLab } from "../data/site.js";

export default function TextLabPage({ current, onNavigate}) {
    return (
        <AnimatedCardGrid className="dashboard-grid">
            <article className="hero-stage panel-full">
                <Nav current={current} onNavigate={onNavigate} />
                <PageHeading title={textLab.heroTitle} description={textLab.heroSubtitle} />
            </article>

            <InputCard />
            <ResultCard />
        </AnimatedCardGrid>
    );
}