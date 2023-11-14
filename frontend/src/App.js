import 'bootstrap/dist/css/bootstrap.min.css';
import {Routes, Route, BrowserRouter} from "react-router-dom";

import Layout from "./hocs/Layout";

import ChatList from "./components/ChatList";
import Login from "./components/Login";
import Register from "./components/Register";

function App() {
  return (
      <BrowserRouter>
          <Layout>
              <Routes>
                  <Route path={"*"} element={ <ChatList/> }/>
                  <Route path={"/login"} element={ <Login/> }/>
                  <Route path={'/register'} element={ <Register/> }/>
              </Routes>
          </Layout>
      </BrowserRouter>
  );
}

export default App;
