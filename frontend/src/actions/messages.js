import Cookies from "js-cookie";
import axios from "axios";
import {CHAT_MESSAGES_FETCH_FAIL, CHAT_MESSAGES_FETCH_SUCCESS} from "./types";

export const getChatMessages = (chat_id) => async dispatch => {
    const config = {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken')
        },
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFTOKEN',
        withCredentials: true
    };

    try {
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/chats/${chat_id}/messages`, config)

        if (res.status === 200) {
            dispatch({
                type: CHAT_MESSAGES_FETCH_SUCCESS,
                payload: {
                    chat_id: chat_id,
                    messages: res.data
                }
            })
        } else {
            dispatch({
                type: CHAT_MESSAGES_FETCH_FAIL
            })
            console.log(`CHAT MESSAGES GET ERROR: ${res.status} STATUS CODE`)
        }
    } catch (err) {
        dispatch({
            type: CHAT_MESSAGES_FETCH_FAIL
        })
        console.log(`CHAT MESSAGES GET ERROR: ${err}`)
    }
}
