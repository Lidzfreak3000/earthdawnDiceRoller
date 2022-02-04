import ResultsText from "./text";
import { Tab, Tabs } from "react-bootstrap";
import "./results.css"
import Results2D from "./2d";

function Results(props) {
    return (
        <Tabs
            defaultActiveKey="text"
            id="tab-menu"
            className="mb-3"
            fill
        >
            <Tab eventKey="text" title="Text">
                <ResultsText />
            </Tab>
            <Tab eventKey="2d" title="2D Roll">
                <Results2D />
            </Tab>
            <Tab eventKey="3d" title="3D Roll">
                blergh 2
            </Tab>
        </Tabs >
    );
}

export default Results;