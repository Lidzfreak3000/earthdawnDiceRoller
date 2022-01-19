import { Tabs, Tab } from 'react-bootstrap';
import Steps from './steps';

function Menu(props) {
    return (
        <Tabs
            defaultActiveKey="steps"
            id="tab-menu"
            className="mb-3"
            fill
        >
            <Tab eventKey="steps" title="Steps">
                <Steps buttons={[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}/>
            </Tab>
            <Tab eventKey="custom" title="Custom Roll">
                blergh 2
            </Tab>
        </Tabs>
    );
}

export default Menu;