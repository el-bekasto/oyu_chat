import Cookies from "js-cookie";
import axios from "axios";
import {
    CHAT_FETCH_FAIL,
    CHATS_FETCH_SUCCESS,
} from "./types";


export const getChats = () => async dispatch => {
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
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/chats`, config);

        if (res.status === 200) {
            dispatch({
                type: CHATS_FETCH_SUCCESS,
                payload: res.data
            });
        } else {
            dispatch({
                type: CHAT_FETCH_FAIL
            });
        }
    } catch (err) {
        dispatch({
            type: CHAT_FETCH_FAIL
        });
    }
}