import 'bootstrap/dist/css/bootstrap.min.css';

import Layout from "./hocs/Layout";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import ChatList from "./components/ChatList";
import Login from "./components/Login";
import Register from "./components/Register";
import PrivateRoute from "./hocs/PrivateRoute";
import {useEffect, useState} from "react";
import {checkAuthentication} from "./actions/auth";
import {connect} from "react-redux";
import {Oval} from "react-loader-spinner";
import './styles/App.css'

function App({ checkAuthentication }) {
    const [checkingAuthentication, setCheckingAuthentication] = useState(true);

    useEffect(() => {
        const check = async () => {
            await checkAuthentication();
        }
        check();
        setCheckingAuthentication(false);
    }, []);

    if (checkingAuthentication) {
        return (<Oval color={'blue'} secondaryColor={'white'}/>);
    }

  return (
      <BrowserRouter>
        <Layout>
          <Routes>
              <Route
                  path={"*"}
                  element={
                    <PrivateRoute>
                        <ChatList/>
                    </PrivateRoute>
                  }
              />
              <Route path={"/login"} element={ <Login/> }/>
              <Route path={'/register'} element={ <Register/> }/>
          </Routes>
        </Layout>
      </BrowserRouter>
  );
}

export default connect(null, {checkAuthentication})(App);
