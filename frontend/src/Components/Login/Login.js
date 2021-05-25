import React, {useState} from 'react'
import "./Login.css"

function Login() {
    const [user, setUser] = useState(
        {
            username: "",
            password: ""
        }
    )
    const [error, setError] = useState(false)

    const handleChange = (e) => {
        const {id, value} = e.target
        setUser(prevState => ({
            ...prevState,
            [id] : value
        }))
    }

    const handleSubmitClick = (e) => {
        e.preventDefault()
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        }
        fetch(`auth/`, requestOptions)
            .then(response => response.json())
            .then((res) => {
                if (res.token && res.user_id) {
                  localStorage.clear();
                  localStorage.setItem('token', res.token);
                  localStorage.setItem('user_id', res.user_id)
                  setError(false);
                  window.location.replace('/');
                } else {
                  localStorage.clear();
                  setError(true);
                }
            },
            (error) => {
                console.log(error)
            })
    }

    return (
        <div className={"login"}>
            <div className={"login-triangle"}/>

            <h2 className={"login-header"}>Log in</h2>

            <form className={"login-container"}>
                {error && <p className={"error"}>You have entered incorrect username or password! Please try again.</p>}
                <p><input id={"username"} type={"username"} placeholder={"Username"} onChange={handleChange} required/></p>
                <p><input id={"password"} type={"password"} placeholder={"Password"} onChange={handleChange} required/></p>
                <p><input type={"submit"} value={"Log in"} onClick={handleSubmitClick}/></p>
            </form>
        </div>
    )
}

export default Login