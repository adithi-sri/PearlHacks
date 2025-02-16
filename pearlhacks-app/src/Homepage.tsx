import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Leaderboard from "./components/Leaderboard";
import User from "./components/User";
import Login from "./components/login";
import Register from "./components/Register";
import "./App.css";
import Timer from "./components/Timer";

function Homepage() {
  return (
    <div>
      <Timer></Timer>
      <Leaderboard />
      <User></User>
    </div>
  );
}

export default Homepage;
