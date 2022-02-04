import { Tabs, Tab } from 'react-bootstrap';
import CustomRoll from './custom';
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
                <Steps />
            </Tab>
            <Tab eventKey="custom" title="Custom Roll">
                <CustomRoll />
            </Tab>
        </Tabs>
    );
}

export default Menu;