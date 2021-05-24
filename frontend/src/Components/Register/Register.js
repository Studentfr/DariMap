import React, {useState} from 'react'
import "./Register.css"

function Register() {

    return (
        <div className={"register"}>
            <div className={"register-triangle"}/>

            <h2 className={"register-header"}>Sign up</h2>

            <form className={"register-container"}>
                <p><input type={"username"} placeholder={"Username"}/></p>
                <p><input type={"password"} placeholder={"Password"}/></p>
                <p><input type={"password"} placeholder={"Re-Password"}/></p>
                <p><input type={"submit"} value={"Register"}/></p>
            </form>
        </div>
    )
}

export default Register