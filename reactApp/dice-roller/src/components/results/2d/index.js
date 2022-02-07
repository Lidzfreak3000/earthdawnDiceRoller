import { useContext } from "react";
import { ResultsContext } from "../../../utils/contexts/ResultsContext";

const ParseInput = (output, value) => {
    const input = value.replace(/([*!`(),])/gm, '');
    const myArray = input.split(" ");
    const conditions = ["+", "="]; //This is used to define what values should be ignored/skipped
    let currentSides = "";

    output.total = myArray.at(-1);

    for (var i = 0; i < (myArray.length - 1); i++) {
        if (conditions.some(el => myArray[i].includes(el))) {
            //Skip that item in the array
        }
        else if (myArray[i].includes("d")) { 
            //Pull out what kind of die was being rolled
            currentSides = myArray[i].substring(
                myArray[i].indexOf("d") + 1,
                myArray[i].indexOf("e")
            );
        }
        else if (myArray[i].includes("-")) { 
            //Ignore subtractions b/c they arent dice rolls
            i++;
        }
        else { 
            //Pull out the actual dice results one at a time
            console.log("else: " + myArray[i]);
            console.log("currentSides: " + currentSides);
            console.log("Current Results: " + JSON.stringify(output));

            output.results.push({
                sides: `${currentSides}`, 
                value: `${parseInt(myArray[i], 10)}`
            });
        }
    }

    return output;
}

function Results2D() {
    const { value } = useContext(ResultsContext);

    let output = {results: [], total: ""};

    if (value) {
        ParseInput(output, value);
    }

    return (
        <div className="TextResults">
            <br />
            {JSON.stringify(output.results) ?? "Please choose a step to roll."}
            <h3>Total: {output.total}</h3>
        </div>
    );
}

export default Results2D;