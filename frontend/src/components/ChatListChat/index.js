import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import './style.css';

export default function ChatListChat ({chatInfo}) {
    function clickChat () {
        // console.log(chatInfo.chatId);
    }
    return (
        <Container className={"chatlistchat"}>
            <Row onClick={clickChat}>
                <Col lg={"2"}>{chatInfo.avatar}</Col>
                <Col lg={"auto"}>
                    <strong>{chatInfo.name}</strong>
                    <p>{chatInfo.lastMessage}</p>
                </Col>
            </Row>
        </Container>
    );
}