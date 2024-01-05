import {useParams} from "react-router-dom";
import {connect} from "react-redux";
import {getChatMessages} from "../actions/messages";
import {Oval} from "react-loader-spinner";
import {useEffect} from "react";
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import '../styles/Chat.css';

function Chat ({ props, getChatMessages, messages }) {
    const params = useParams();
    console.log(messages);
    console.log(params.id);

    // fetch chat messages if they're null
    useEffect(() => {
        const fetchChatMessages = async () => {
            await getChatMessages(params.id);
        }
        if (messages === null || messages[params.id] === null) {
            fetchChatMessages();
        }
    });

    // show loading cycle if messages are null and being fetched
    if (messages === null || messages[params.id] === null) {
        return (<Oval color={'blue'} secondaryColor={'white'}/>)
    }

    return (
        <Container>
            {/*table is list of messages in current chat*/}
            <table>
                {messages[params.id].map((x) => <tr>
                    <b>{x.author.username}</b>
                    <br></br>
                    {x.text}
                </tr>)}
            </table>
            <Form.Control className={"new-message-text"} type={"text"} placeholder={"type message..."}/>

        </Container>
    )
}

const mapStateToProps = state => ({
    messages: state.messages.messages
});

export default connect(mapStateToProps, { getChatMessages })(Chat);