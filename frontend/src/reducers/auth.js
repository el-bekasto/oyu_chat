import {
    AUTHENTICATED_FAIL, AUTHENTICATED_SUCCESS,
    LOGIN_FAIL,
    LOGIN_SUCCESS,
    LOGOUT_FAIL,
    LOGOUT_SUCCESS,
    REGISTER_FAIL,
    REGISTER_SUCCESS
} from "../actions/types";

const initialState = {
    isAuthenticated: null
};

export default function(state=initialState, action) {
    switch (action.type) {
        case LOGOUT_SUCCESS:
        case REGISTER_SUCCESS:
        case AUTHENTICATED_FAIL:
            return {
                ...state,
                isAuthenticated: false
            }
        case LOGIN_SUCCESS:
        case AUTHENTICATED_SUCCESS:
            return {
                ...state,
                isAuthenticated: true
            }
        case REGISTER_FAIL:
        case LOGIN_FAIL:
        case LOGOUT_FAIL:
        default:
            return state
    }
}