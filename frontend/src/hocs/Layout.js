import NavbarComponent from '../components/Navbar';
import {connect} from "react-redux";
import {Fragment} from "react";

function Layout ({ isAuthenticated, children }) {
    return (
        <Fragment>
            {isAuthenticated ? <NavbarComponent/> : null}
            {children}
        </Fragment>
    )
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, {})(Layout);