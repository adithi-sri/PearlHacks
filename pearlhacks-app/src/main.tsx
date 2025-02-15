import React from 'react'
import ReactDOM from 'react-dom/client';
import Login from "./login";
import App from "./App";
import {BrowserRouter} from "react-router-dom";

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(<React.StrictMode> <Login /></React.StrictMode>)
