import {combineReducers} from "@reduxjs/toolkit";
import auth from './auth';
import chats from "./chats";

export default combineReducers({
    auth,
    chats
});