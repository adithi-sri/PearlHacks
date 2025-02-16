import React from 'react'
import ReactDOM from 'react-dom/client';
import Login from "./components/login";
import Register from "./components/Register";
//import Searching from "./Searching";
import App from "./App";
import 'bootstrap/dist/css/bootstrap.css'
import io from 'socket.io-client';

const socket = io('http://localhost:3000');

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>,
)

//ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(<React.StrictMode> <Login /></React.StrictMode>)
