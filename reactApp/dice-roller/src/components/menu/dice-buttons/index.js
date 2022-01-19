import { Button } from "react-bootstrap";
import './dice-buttons.css';

function Steps(props) {
    return (
        <Button className="diceButton" key={props.key} name={props.name}>
            {props.name}
        </Button>
    );
}

export default Steps;