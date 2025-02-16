import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Leaderboard from "./components/Leaderboard";
import User from "./components/User";
import Login from "./components/login";
import Register from "./components/Register";
import "./App.css";
import Timer from "./components/Timer";
import "./Homepage.css";
import Chatbox from "./components/Chatbox";

function Homepage() {
  return (
    <div>
      <h1 className="home-page">Homepage</h1>
      <h1 className="tim-heading">Study Timer</h1>
      <Timer></Timer>
      <Leaderboard />
      <Chatbox></Chatbox>
      <User></User>
    </div>
  );
}

export default Homepage;
