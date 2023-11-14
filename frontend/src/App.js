import 'bootstrap/dist/css/bootstrap.min.css';
import {Routes, Route, BrowserRouter} from "react-router-dom";

import Layout from "./hocs/Layout";

import ChatList from "./components/ChatList";
import Login from "./components/Login";
import Register from "./components/Register";

function App() {
  return (
      <BrowserRouter>
              <Routes>
                  <Route path={"*"} element={ <ChatList/> }/>
                  <Route path={"/login"} element={ <Login/> }/>
                  <Route path={'/register'} element={ <Register/> }/>
              </Routes>
      </BrowserRouter>
  );
}

export default App;
