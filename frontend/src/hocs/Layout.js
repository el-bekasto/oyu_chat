import NavbarComponent from '../components/Navbar'
import {Fragment} from "react";
import {connect} from "react-redux";
import {logout} from "../actions/auth";
import Login from "../components/Login";
import {Routes, Route, BrowserRouter} from "react-router-dom";
import ChatList from "../components/ChatList";
import Register from "../components/Register";

function Layout ({ isAuthenticated, logout, children }) {
    return (
        <BrowserRouter>
            {isAuthenticated ? <NavbarComponent/> : null}
            <Routes>
                <Route path={"*"} element={ isAuthenticated ? <ChatList/> : <Login/> }/>
                <Route path={"/login"} element={ <Login/> }/>
                <Route path={'/register'} element={ <Register/> }/>
            </Routes>
        </BrowserRouter>
    )
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { logout })(Layout);