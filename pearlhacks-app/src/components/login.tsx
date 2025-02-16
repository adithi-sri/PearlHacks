import React, {useState} from "react";
import { useNavigate} from "react-router-dom";
import "./Login.css";

function Login() {
    const navigate = useNavigate();

    const handleSignUpClick = () => {
        navigate("/register");
    };
    const handleLogInClick = () => {
        navigate("/homepage");
    }
    return (
        <>
            <p className="title">Login or Register</p>

            <form className="Login">
                <input type="text" placeholder = "name" />
                <input type="password" placeholder = "password"/>
                <button type="submit" onClick={handleLogInClick}>Login</button>
                <button type="submit" onClick={handleSignUpClick}>Sign Up</button>
            </form>

        </>
    );
}

export default Login;