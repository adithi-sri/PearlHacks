import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './login.css';

function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogInClick = async (event: React.FormEvent) => {
        event.preventDefault();
        try {
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (response.ok) {
                const data = await response.json();
                if (data.success) {
                    navigate('/homepage');
                } else {
                    setError(data.message || 'Invalid username or password');
                }
            } else {
                setError('Invalid username or password');
            }
        } catch (error) {
            setError('An error occurred');
        }
    };

    const handleSignUpClick = (event: React.FormEvent) => {
        event.preventDefault();
        navigate('/register');
    };

    return (
        <>
            <p className="title">Login or Register</p>

            <form className="Login">
                <input
                    type="text"
                    placeholder="name"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit" onClick={handleLogInClick}>Login</button>
                <button type="submit" onClick={handleSignUpClick}>Sign Up</button>
            </form>
            {error && <p className="error">{error}</p>}
        </>
    );
}

export default Login;