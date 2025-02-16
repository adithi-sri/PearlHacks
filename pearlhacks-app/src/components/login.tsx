import React, {useState} from "react";
import "./login.css";

function Login() {
    return (
        <>
            <p className="title">Login or Register</p>

            <form className="Login">
                <input type="name" placeholder = "name" />
                <input type="password" placeholder = "password"/>
                <input type="submit" value="Log In"/>
                <input type="submit" value="Sign Up"/>
            </form>
        </>
    );
}

export default Login;