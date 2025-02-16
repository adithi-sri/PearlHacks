// filepath: /Users/rucha/OneDrive/Desktop/pearlhacks/PearlHacks/pearlhacks-app/src/components/Register.tsx
import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import "./register.css";

function Register() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSignUpClick = async (event: React.FormEvent) => {
        event.preventDefault();
        navigate("/homepage")
    }

    return (
        <>
            <p className="title">Enter your information!</p>

            <form className="Register" onSubmit={handleSignUpClick}>
                <input
                    type="text"
                    id="name"
                    placeholder="Enter your full name"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    id="password"
                    placeholder="Enter a password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <input type="text" id="course1" placeholder="Enter a course code. Ex: COMP 210" />
                <input type="text" id="course2" placeholder="Enter a course code. Ex: COMP 210" />
                <input type="text" id="course3" placeholder="Enter a course code. Ex: COMP 210" />
                <input type="text" id="course4" placeholder="Enter a course code. Ex: COMP 210" />
                <input type="text" id="course5" placeholder="Enter a course code. Ex: COMP 210" />
                <input type="text" id="course6" placeholder="Enter a course code. Ex: COMP 210" />
                <button type="submit">Register</button>
            </form>
            {error && <p className="error">{error}</p>}
        </>
    );
}

export default Register;