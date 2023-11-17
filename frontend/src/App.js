import 'bootstrap/dist/css/bootstrap.min.css';

import Layout from "./hocs/Layout";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import ChatList from "./components/ChatList";
import Login from "./components/Login";
import Register from "./components/Register";
import PrivateRoute from "./hocs/PrivateRoute";

function App() {
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

export default App;
