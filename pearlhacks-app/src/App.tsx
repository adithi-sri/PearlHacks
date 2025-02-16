import React from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Leaderboard from "./components/Leaderboard";
<<<<<<< HEAD
import User from "./components/User";
import Login from "./components/login";
import Register from "./components/Register";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/leaderboard" element={<Leaderboard/>}/>
      </Routes>
    </Router> 
=======
import { Routes, Route } from "react-router-dom";
import User from "./components/User";
import "./App.css";
//import Login from "./login";
//import Register from "./register";
//import Searching from "./Searching";

function App() {
  return (
    <div className="main-page">
      <Leaderboard />
      <User></User>
    </div>
>>>>>>> 890fb41 (h)
  );
}

export default App;
