import Cookies from "js-cookie";
import axios from "axios";

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
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/v1/getChats`, config);
        console.log(res);
    } catch (err) {

    }
}