import {CHAT_MESSAGES_FETCH_FAIL, CHAT_MESSAGES_FETCH_SUCCESS} from "../actions/types";

const initialState = {
    messages: null
}

export default function(state=initialState, action) {
    switch (action.type) {
        case CHAT_MESSAGES_FETCH_SUCCESS:
            return {
                ...state,
                messages: {
                    ...state.messages,
                    [action.payload.chat_id]: action.payload.messages
                }
            }
        case CHAT_MESSAGES_FETCH_FAIL:
        default:
            return state
    }
}