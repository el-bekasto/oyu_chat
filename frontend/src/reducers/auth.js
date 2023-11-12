import {LOGIN_FAIL, LOGIN_SUCCESS, REGISTER_FAIL, REGISTER_SUCCESS} from "../actions/types";

const initialState = {
    isAuthenticated: null
};

export default function(state=initialState, action) {
    switch (action.type) {
        case REGISTER_SUCCESS:
            return {
                ...state,
                isAuthenticated: false
            }
        case LOGIN_SUCCESS:
            return {
                ...state,
                isAuthenticated: true
            }
        case REGISTER_FAIL:
        case LOGIN_FAIL:
        default:
            return state
    }
}