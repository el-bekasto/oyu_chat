import NavbarComponent from '../components/Navbar'
import {Fragment} from "react";
import {connect} from "react-redux";
import {logout} from "../actions/auth";
import Login from "../components/Login";
import {Routes, Route, BrowserRouter} from "react-router-dom";
import ChatList from "../components/ChatList";
import Register from "../components/Register";

function Layout ({ isAuthenticated, children }) {
    return (
        <div>
            {isAuthenticated ? <NavbarComponent/> : null}
            {children}
        </div>
    )
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { logout })(Layout);