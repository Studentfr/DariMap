import React from 'react'
import "./Login.css"

function Login() {
    return (
        <div className={"login"}>
            <div className={"login-triangle"}/>

            <h2 className={"login-header"}>Log in</h2>

            <form className={"login-container"}>
                <p><input type={"username"} placeholder={"Username"}/></p>
                <p><input type={"password"} placeholder={"Password"}/></p>
                <p><input type={"submit"} value={"Log in"}/></p>
            </form>
        </div>
    )
}

export default Login