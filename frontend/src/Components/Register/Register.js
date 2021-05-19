import React from 'react'
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
                <p>
                    <select name={"roles"} id={"roles"}>
                        <option value={"client"}>Client</option>
                        <option value={"pharmacy"}>Pharmacy</option>
                    </select>
                </p>
                <p><input type={"submit"} value={"Register"}/></p>
            </form>
        </div>
    )
}

export default Register