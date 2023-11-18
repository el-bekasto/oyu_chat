import Row from "react-bootstrap/Row";
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';

export default function Chat ({chat}) {
    const openChat = () => {
        return (<h1>fuck</h1>)
    }

    return (
        <Container onClick={openChat}>
            <Row>
                {/*<Col>*/}
                    {/*{chat.avatar ? <img src={}>}*/}
                {/*</Col>*/}
                <Col>
                    {chat.name}
                </Col>
                <Col>
                    {chat.created_at}
                </Col>
            </Row>
        </Container>
    )
}