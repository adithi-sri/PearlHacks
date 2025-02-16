import { useState, useEffect, useRef } from "react";
import "./Timer.css";

function Timer() {
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [elapsedTime, setElapsedTime] = useState<number>(0);
  const intervalIdRef = useRef<NodeJS.Timeout | null>(null);
  const startTimeRef = useRef<number>(0);
  const username = "your_username"; // Replace with the actual username

  useEffect(() => {
    if (isRunning) {
      intervalIdRef.current = setInterval(() => {
        setElapsedTime(Date.now() - startTimeRef.current);
      }, 10);
    } else if (intervalIdRef.current) {
      clearInterval(intervalIdRef.current);
    }

    return () => {
      if (intervalIdRef.current) clearInterval(intervalIdRef.current);
    };
  }, [isRunning]);

  function start() {
    setIsRunning(true);
    startTimeRef.current = Date.now() - elapsedTime;
    fetch("/start_session", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: `username=${username}`
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === "success") {
        console.log(data.message);
      } else {
        console.error(data.message);
      }
    });
  }

  function stop() {
    setIsRunning(false);
    fetch("/end_session", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: `username=${username}`
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === "success") {
        console.log(data.message);
      } else {
        console.error(data.message);
      }
    });
  }

  function reset() {
    setElapsedTime(0);
    setIsRunning(false);
  }

  function formatTime(): string {
    let hours = Math.floor(elapsedTime / (1000 * 60 * 60));
    let minutes = Math.floor((elapsedTime / (1000 * 60)) % 60);
    let seconds = Math.floor((elapsedTime / 1000) % 60);
    let milliseconds = Math.floor((elapsedTime % 1000) / 10);

    const pad = (num: number) => String(num).padStart(2, "0");

    return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}:${pad(milliseconds)}`;
  }

  return (
    <div className="stopwatch">
      <div className="display">{formatTime()}</div>
      <div className="controls">
        <button onClick={start} className="start-button">
          Start
        </button>
        <button onClick={stop} className="stop-button">
          Stop
        </button>
        <button onClick={reset} className="reset-button">
          Reset
        </button>
      </div>
    </div>
  );
}

export default Timer;
