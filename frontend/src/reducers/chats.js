import {CHAT_FETCH_FAIL, CHATS_FETCH_SUCCESS} from "../actions/types";

const initialState = {
    chats: null
}

export default function(state=initialState, action) {
    switch (action.type) {
        case CHATS_FETCH_SUCCESS:
            return {
                ...state,
                chats: action.payload
            }
        case CHAT_FETCH_FAIL:
        default:
            return state
    }
}