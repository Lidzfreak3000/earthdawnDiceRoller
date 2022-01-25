import { Button } from "react-bootstrap";
import { useContext } from "react";
import './dice-buttons.css';
import { ResultsContext } from "../../../utils/contexts/ResultsContext";

function Steps(props) {
    const { setValue } = useContext(ResultsContext);

    const RollDice = (stepNum) => {
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
            "step": stepNum
        });

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
        };

        fetch("https://earthdawn.azurewebsites.net/api/diceRoller?code=Lo5iYjcCHH9gM7MqhS2Fus5fCEOeLopg3jvpXhw0vdMmeUHLkawDqg==", requestOptions)
            .then(res => res.text())
            .then(
                (result) => {
                    setValue(result);
                })
            .catch(error => console.log('error', error));
    }

    const handleChange = event => {
        RollDice(event.target.name);
    };

    return (
        <Button className="diceButton" key={props.key} name={props.name} onClick={handleChange}>
            {props.name}
        </Button>
    );
}

export default Steps;