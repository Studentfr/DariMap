import React, {useState} from 'react'
import "./Register.css"

function Register() {
    const [newUser, setNewUser] = useState({
        username: "",
        password: "",
        confirmation: ""
    })
    const [error, setError] = useState("")

    const handleChange = (e) => {
        const {id, value} = e.target
        setNewUser(prevState => ({
            ...prevState,
            [id] : value
        }))
    }

    const handleSubmitClick = (e) => {
        e.preventDefault()
        if (newUser.password === newUser.confirmation) {
            const requestBody = {
                username: newUser.username,
                password: newUser.password,
                groups: [],
                user_permissions: [],
                role_id: 2
            }
            const requestOptions = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestBody)
            }
            fetch(`api/users/`, requestOptions)
                .then(response => response.json())
                .then((res) => {
                    if (res.id) {
                      setError("")
                      window.location.replace('/');
                    } else {
                      setError("User with such username already exists. Please, try again.");
                    }
                },
                (error) => {
                    console.log(error)
                })
        } else {
            setError("Error! Passwords are not equal. Please, try again.")
        }
    }

    return (
        <div className={"register"}>
            <div className={"register-triangle"}/>

            <h2 className={"register-header"}>Sign up</h2>

            <form className={"register-container"}>
                {error && <p className="error">{error}</p>}
                <p><input id={"username"} type={"username"} placeholder={"Username"} onChange={handleChange}/></p>
                <p><input id={"password"} type={"password"} placeholder={"Password"} onChange={handleChange}/></p>
                <p><input id={"confirmation"} type={"password"} placeholder={"Re-Password"} onChange={handleChange}/></p>
                <p><input type={"submit"} value={"Register"} onClick={handleSubmitClick}/></p>
            </form>
        </div>
    )
}

export default Register