import { useContext } from "react";
import { ResultsContext } from "../../../utils/contexts/ResultsContext";

function Results2D() {
    const { value } = useContext(ResultsContext);

    let output = "";
    let input = "";
    const conditions = ["+", "=", "d"];

    input = value.replace(/([*!`(),])/gm, '');
    console.log(input);

    const myArray = input.split(" ");
    const total = myArray.at(-1);

    for (var i = 0; i < (myArray.length-1); i++) {
        console.log(myArray[i]);

        if (conditions.some(el => myArray[i].includes(el))) {
            output += "";
        }
        else if (myArray[i].includes("-"))
        {
            i++;
        }
        else {
            output += parseInt(myArray[i], 10);
        }
    }

    return (
        <div className="TextResults">
            <br />
            {output}
            <h3>Total: {total}</h3>
        </div>
    );
}

export default Results2D;