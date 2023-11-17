import ChatList from "../components/ChatList";
import {Navigate} from "react-router-dom";
import {Route} from "react-router-dom";
import {connect} from "react-redux";

function PrivateRoute ({ isAuthenticated, children }) {
    if (!isAuthenticated) {
        return <Navigate to={'/login'}/>
    }

    return children;
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, {})(PrivateRoute);
