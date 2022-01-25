import { useContext } from "react";
import { ResultsContext } from "../../../utils/contexts/ResultsContext";

function ResultsText() {
    const { value } = useContext(ResultsContext);

    return (
        <div className="TextResults">
            <br/>
            {value}
        </div>
    );
}

export default ResultsText;