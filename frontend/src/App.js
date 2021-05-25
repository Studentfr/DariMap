import React, {useEffect, useState} from 'react'
import Sidebar from "./Components/Sidebar/Sidebar";
import Map from "./Components/Map/Map";
import DrugSearch from "./Components/Sidebar/DrugSearch";
import Navbar from "./Components/Navbar/Navbar";
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Register from "./Components/Register/Register";
import Login from "./Components/Login/Login";
import Cabinet from "./Components/Cabinet/Cabinet";

function App() {

    const [pharmacies, setPharmacies] = React.useState([])
    const [pharmacyId, setPharmacyId] = React.useState(0)
    const [previewVisibility, setPreviewVisibility] = React.useState(false)
    const [drugVisibility, setDrugVisibility] = React.useState(false)
    const [loggedIn, setLoggedIn] = useState(false)
    const [favPharmacies, setFavPharmacies] = useState(
        [
            {
                id: 0,
                pharmacy_id: {
                    id: 0,
                    name: "",
                    address: "",
                    phone_number: ""
                }
            }
        ]
    )

    useEffect(() => {
        fetch('api/pharmacy-list')
            .then(response => response.json())
            .then((pharmacies) => {
                setPharmacies(pharmacies)
                console.log(pharmacies)
            },
            (error) => {
                setPharmacies(mockPharmacies)
                console.log(error)
            })

        if (localStorage.getItem('token') !== null) {
            setLoggedIn(true)
        } else {
            setLoggedIn(false)
        }
    }, [])

    useEffect(() => {
        if (loggedIn) {
            fetch(`api/favourite-pharmacy-list/${localStorage.getItem('user_id')}`)
                .then(response => response.json())
                .then((pharmacies) => {
                    setFavPharmacies(pharmacies)
                    console.log(pharmacies)
                },
                (error) => {
                    console.log(error)
                })
        }
    }, [loggedIn])

    const mockPharmacies = [
        {
            id: 1,
            name: 'Здоровье',
            coordinate_id: {
                latitude: 51.097906,
                longitude: 71.414127
            }
        },
        {
            id: 2,
            name: 'Солнечный',
            coordinate_id: {
                latitude: 51.088947,
                longitude: 71.442401
            }
        },
        {
            id: 3,
            name: 'Северный',
            coordinate_id: {
                latitude: 51.134889,
                longitude: 71.462434
            }
        },
        {
            id: 4,
            name: 'Семейный',
            coordinate_id: {
                latitude: 51.152443,
                longitude: 71.440453
            }
        },
        {
            id: 5,
            name: 'Социальная аптека',
            coordinate_id: {
                latitude: 51.155555,
                longitude: 71.465755
            }
        },
    ]

    const getSelectedPharmacyId = (id) => {
        setPharmacyId(id)
        if (pharmacyId === id || (!previewVisibility && pharmacyId !== id)) {
            togglePreviewVisibility()
        }
        setDrugVisibility(false)
    }

    const togglePreviewVisibility = () => {
        setPreviewVisibility(!previewVisibility)
    }

    const closeDescription = () => {
        setPreviewVisibility(false)
        setDrugVisibility(false)
    }

    const getFavPharmacy = (pharmacyId) => {
        const val = favPharmacies.filter((pharmacy) => pharmacy.pharmacy_id.id === pharmacyId)
        if (val.length === 0) {
            return false
        }
        return favPharmacies.filter((pharmacy) => pharmacy.pharmacy_id.id === pharmacyId)[0]
    }

    const addFavPharmacy = (pharmacyId) => {
        const requestBody = {
                user_id: parseInt(localStorage.getItem("user_id")),
                pharmacy_id: pharmacyId
            }
            const requestOptions = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestBody)
            }
            fetch(`api/favourite-pharmacy-create/`, requestOptions)
                .then(response => response.json())
                .then(() => {
                    fetch(`api/favourite-pharmacy-list/${localStorage.getItem('user_id')}`)
                        .then(response => response.json())
                        .then((pharmacies) => {
                            setFavPharmacies(pharmacies)
                            console.log(pharmacies)
                        },
                        (error) => {
                            console.log(error)
                        })
                },
                (error) => {
                    console.log(error)
                })
    }

    const deleteFavPharmacy = (pharmacyId) => {
        const id = favPharmacies.filter((favPharmacy) => favPharmacy.pharmacy_id.id === pharmacyId )[0].id
        const requestOptions = {
            method: 'DELETE'
        }
        fetch(`api/favourite-pharmacy-delete/${id}/`, requestOptions)
            .then(response => response.json())
            .then(() => {
                setFavPharmacies(favPharmacies.filter((pharmacy) => pharmacy.id !== id))
            },
            (error) => {
                console.log(error)
            })
    }

    return (
        <Router>
            <div>
                <Navbar loggedIn={loggedIn} setLoggedIn={setLoggedIn}/>
                <Switch>
                    <Route exact path="/">
                        <DrugSearch id={pharmacyId} isVisible={drugVisibility} closeDrugDescription={setDrugVisibility}/>
                        <Sidebar getFavPharmacy={getFavPharmacy} addFavPharmacy={addFavPharmacy} deleteFavPharmacy={deleteFavPharmacy} id={pharmacyId} isVisible={previewVisibility} closeDescription={closeDescription} openDrugs={setDrugVisibility} loggedIn={loggedIn} />
                        <Map pharmacies={pharmacies} onPharmacySelect={getSelectedPharmacyId}/>
                    </Route>
                    <Route path="/login">
                        <Login/>
                    </Route>
                    <Route path="/register">
                        <Register/>
                    </Route>
                    <Route path="/cabinet">
                        <Cabinet favPharmacies={favPharmacies} setFavPharmacies={setFavPharmacies}/>
                    </Route>
                </Switch>
            </div>
        </Router>
    )
}

export default App;
