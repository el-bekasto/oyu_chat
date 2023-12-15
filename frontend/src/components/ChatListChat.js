import Row from "react-bootstrap/Row";
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Chat from "./Chat";
import {Navigate, useNavigate} from "react-router-dom";

export default function ChatListChat ({chat}) {
    const navigate = useNavigate();
    const openChat = () => {
        console.log('here i am')
        navigate(`/chat/${chat.id}`)
    }

    return (
        <Container>
            <Row>
                <a href={'javascript:void(0)'} onClick={openChat} className={'stretched-link'}/>
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