import 'bootstrap/dist/css/bootstrap.min.css';
import {Routes, Route, BrowserRouter} from "react-router-dom";

import Layout from "./hocs/Layout";

import ChatList from "./containers/ChatList";
import Login from "./containers/Login";

function App() {
  return (
      <BrowserRouter>
          <Layout>
              <Routes>
                  <Route path={"/"} element={ <ChatList/> }/>
                  <Route path={"/login"} element={ <Login/> }/>
              </Routes>
          </Layout>
      </BrowserRouter>
  );
}

export default App;
