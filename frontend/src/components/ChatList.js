import {connect} from "react-redux";
import Chat from "./Chat";
import {getChats} from "../actions/chats";
import {useEffect, useState} from "react";
import {Oval} from "react-loader-spinner";

function ChatList ({ chats, getChats }) {
    useEffect(() => {
        const fetchChats = async () => {
            await getChats();
        }
        if (chats === null) {
            fetchChats();
        }
    });

    if (chats === null) {
        return (<Oval color={'blue'} secondaryColor={'white'}/>);
    }

    return (
        <div>
            {chats.map((x) =>
                <Chat chat={x}/>
            )}
        </div>
    )
}

const mapStateToProps = state => ({
    chats: state.chats.chats
});

export default connect(mapStateToProps, { getChats })(ChatList);