import React from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Leaderboard from "./components/Leaderboard";
import User from "./components/User";
import Login from "./components/login";
import Register from "./components/Register";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/register" element={<Register/>}/>
      </Routes>
    </Router> 
  );
}

export default App;
