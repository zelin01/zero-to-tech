import { userEffect, useState } from "react";

export function useRoute(){
    const [path, setPath] = useState(window.location.pathname);

    useEffect(() => {
        const handler = () => setPath(window.location.pathname);
        window.addEventListener("popstate", handler);
        return () => window.removeEventListener("popstate", handler);
    }, []);

    function navigate(to){
        if(to === path) return;
        window.history.pushState({}, "", to);
        setPath(to);
    }

    return {path, navigate};
}