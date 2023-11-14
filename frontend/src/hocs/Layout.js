import NavbarComponent from '../components/Navbar'
import {Fragment} from "react";

export default function Layout ({ children }) {
    return (
        <Fragment>
            <NavbarComponent/>
            {children}
        </Fragment>
    )
}