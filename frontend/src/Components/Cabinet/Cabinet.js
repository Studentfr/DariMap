import "./Cabinet.css"
import {useEffect, useState} from "react";

function Cabinet({favPharmacies, setFavPharmacies}) {


    const deleteFavPharmacy = (id) => (e) => {
        e.preventDefault()
        console.log(`DELETE PHARMACY WITH ID = ${id}`)
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
        <div className="limiter">
            <div className="container-table100">
                <div className="wrap-table100">
                    <div className="table">
                        <div className="row header">
                            <div className="cell">
                                Favourite Pharmacies
                            </div>
                            <div className="cell">
                            </div>
                        </div>
                        {favPharmacies.map((pharmacy) => {
                            return (
                                <div className="row" key={pharmacy.id}>

                                    <div className="cell" data-title="Pharmacies">
                                        <p>{pharmacy.pharmacy_id.name}</p>
                                        <p>{pharmacy.pharmacy_id.address}</p>
                                        <p>{pharmacy.pharmacy_id.phone_number}</p>
                                    </div>
                                    <div className="cell" data-title="Delete">
                                        <button type="button" className="delete" onClick={deleteFavPharmacy(pharmacy.id)}>Delete</button>
                                    </div>
                                </div>
                            )
                        })}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Cabinet
