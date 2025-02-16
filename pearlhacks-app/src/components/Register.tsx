import React from "react";
import { useNavigate } from 'react-router-dom';
import "./register.css";

function Register() {
    const navigate = useNavigate();
    const handleSignUpClick = () => {
        navigate('/homepage');
      };
    return (
        <>
            <p className="title">Enter your information!</p>

            <form className="Register">
                <input type="text" id = "name" placeholder = "Enter your full name" />
                <input type="password" id = "password" placeholder = "Enter a password"/>
                <input type="text" id = "course1" placeholder = "Enter a course code. Ex: COMP 210"/>
                <input type="text" id = "course2" placeholder = "Enter a course code. Ex: COMP 210"/>
                <input type="text" id = "course3" placeholder = "Enter a course code. Ex: COMP 210"/>
                <input type="text" id = "course4" placeholder = "Enter a course code. Ex: COMP 210"/>
                <input type="text" id = "course5" placeholder = "Enter a course code. Ex: COMP 210"/>
                <input type="text" id = "course6" placeholder = "Enter a course code. Ex: COMP 210"/>
                <button type="submit" onClick={handleSignUpClick} >Register</button>
            </form>
        </>
    );
}

export default Register;