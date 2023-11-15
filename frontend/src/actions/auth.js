import Cookies from 'js-cookie';
import axios from "axios";
import {REGISTER_SUCCESS, REGISTER_FAIL, LOGIN_SUCCESS, LOGIN_FAIL} from "./types";


export const login = (username, password) => async dispatch => {
    const config = {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken')
        }
    }

    const body = JSON.stringify({ username, password });
    try {
        const res = await axios.post(`${process.env.REACT_APP_API_URL}/sessionAuth/login/`)

        if (res.data.ok) {
            dispatch({
                type: LOGIN_SUCCESS
            });
        } else {
            dispatch({
                type: LOGIN_FAIL
            });
        }
    } catch (error) {
        dispatch({
            type: LOGIN_FAIL
        });
    }
};


export const register = (username, password, re_password) => async dispatch => {
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

    const body = JSON.stringify({username, password, re_password});

    try {
        const res = await axios.post(
            `${process.env.REACT_APP_API_URL}/sessionAuth/register/`,
            body,
            config
        );

        if (res.data.error) {
            dispatch({
                type: REGISTER_FAIL
            });
        } else {
            dispatch({
                type: REGISTER_SUCCESS
            })
        }
    } catch (error) {
        dispatch({
            type: REGISTER_FAIL
        });
    }
}
