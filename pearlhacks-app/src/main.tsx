import React from 'react'
import ReactDOM from 'react-dom/client';
import Login from "./components/login";
import Register from "./components/Register";
//import Searching from "./Searching";
import App from "./App";
import 'bootstrap/dist/css/bootstrap.css';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>,
)

//ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(<React.StrictMode> <Login /></React.StrictMode>)
