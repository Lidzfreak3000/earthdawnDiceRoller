import { useContext } from "react";
import { ResultsContext } from "../../../utils/contexts/ResultsContext";
import "./2d.css";
import DiceSVG from "./diceSVG";

const ParseInput = (output, value) => {
    const input = value.replace(/([*!`(),])/gm, '');
    const myArray = input.split(" ");
    const conditions = ["+", "="]; //This is used to define what values should be ignored/skipped
    let currentSides = "";
    let skip = false;

    output.total = myArray.at(-1);

    myArray.forEach((item) => {
        if (conditions.some(el => item.includes(el))) {
            //Skip that item in the array
        }
        else if (item.includes("d")) {
            //Pull out what kind of die was being rolled
            currentSides = item.substring(
                item.indexOf("d") + 1,
                item.indexOf("e")
            );
        }
        else if (item.includes("-")) {
            //Ignore subtractions b/c they arent dice rolls
            skip = true;
        }
        else {
            //Pull out the actual dice results one at a time
            if (!skip) {
                output.results.push({
                    sides: `${currentSides}`,
                    value: `${parseInt(item, 10)}`
                });
                skip = false;

                console.log("else: " + item);
                console.log("currentSides: " + currentSides);
                console.log("Current Results: " + JSON.stringify(output));
            }
        }
    });

    return output;
}

function Results2D() {
    const { value } = useContext(ResultsContext);

    let output = { results: [], total: "" };

    if (value) {
        ParseInput(output, value);
    }

    return (
        <div className="TextResults">
            <h3>Total: {output.total}</h3>
            <div className="grid">
                {Object.values(output.results).map((item) => (
                    <grid-item>
                        {console.log(JSON.stringify(item))}
                        <DiceSVG sides={item.sides} value={item.value} />
                    </grid-item>
                ))}
            </div>
        </div>
    );
}

export default Results2D;