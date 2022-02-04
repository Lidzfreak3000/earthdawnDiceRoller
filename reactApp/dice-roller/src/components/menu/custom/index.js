import { Form, Button } from "react-bootstrap";

function CustomRoll() {
    return (
    <Form>
        <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Custom Roll String</Form.Label>
            <Form.Control type="text" placeholder="Dice command here..." />
        </Form.Group>
        <Button variant="primary" type="submit">
            Submit
        </Button>
    </Form>
    );
}

export default CustomRoll;