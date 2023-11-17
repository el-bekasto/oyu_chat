import {getChats} from "../actions/chats";
import {connect} from "react-redux";

function ChatList ({getChats}) {
    getChats();

    return (
        <div>
            Chatlist
        </div>
    )
}

export default connect(null, {getChats})(ChatList);