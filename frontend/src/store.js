import rootReducer from './reducers';
import {createStore} from "redux";
import {configureStore} from "@reduxjs/toolkit";

const initialState = {};
export default configureStore({
    reducer: rootReducer
});