import Row from "react-bootstrap/Row";
import Col from 'react-bootstrap/Col';

export default function Chat ({chat}) {
    return (
        <Row>
            <Col>
                chat.name
            </Col>
            <Col>
                chat
            </Col>
        </Row>
    )
}