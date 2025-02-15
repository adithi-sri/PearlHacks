import React from "react";

function Login() {
    return (
        <>
            <p className="title">Registration Form</p>

            <form className="App">
                <input type="text" />
                <input type="email" />
                <input type="password" />
                <input type={"submit"}
                    style={{ backgroundColor: "#a1eafb" }} />
            </form>
        </>
    );
}

export default Login;