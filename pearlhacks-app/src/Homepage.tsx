import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Leaderboard from "./components/Leaderboard";
import User from "./components/User";
import Login from "./components/login";
import Register from "./components/Register";
import "./App.css";
import Timer from "./components/Timer";
import "./Homepage.css";

function Homepage() {
  const items = ["COMP 110", "COMP 283", "LFIT 59", "RELI 073H", "JAPN 162"];
  return (
    <div>
      <h1 className="home-page">Homepage</h1>
      <h1 className="course-head">Courses:</h1>
      <ul className="courses">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
      <h1 className="tim-heading">Study Timer</h1>
      <Timer></Timer>
      <Leaderboard />
      <User></User>
    </div>
  );
}

export default Homepage;
