import React, {useEffect, useState} from 'react'
import { AiFillCloseCircle, AiOutlineStar, AiFillStar } from 'react-icons/ai';
import "./Sidebar.css"
import DrugSearch from "./DrugSearch";

function Sidebar({id, isVisible, closeDescription, openDrugs, loggedIn, getFavPharmacy, addFavPharmacy, deleteFavPharmacy}) {
    const [pharmacy, setPharmacy] = React.useState({})
    const [isFavourite, setIsFavourite] = useState(false)

    useEffect(() => {
        fetch(`api/pharmacy-detail/${id}`)
            .then(response => response.json())
            .then((pharmacy) => {
                setPharmacy(pharmacy)
            },
            (error) => {
                console.log(error)
            })
        if (getFavPharmacy(id) !== false) {
            setIsFavourite(true)
        } else {
            setIsFavourite(false)
        }
    }, [id])

    const toggleFavPharmacy = () => {
        if (isFavourite) {
            deleteFavPharmacy(id)
            setIsFavourite(false)
        } else {
            addFavPharmacy(id)
            setIsFavourite(true)
        }
    }

    return(
        <div className={`preview__container preview__container--${isVisible && id && "active"}`}>
            <div className="preview__close" onClick={() => closeDescription()}>
                <AiFillCloseCircle></AiFillCloseCircle>
            </div>
            <div className="preview__favourite" onClick={toggleFavPharmacy}>
                {loggedIn && !isFavourite && <AiOutlineStar></AiOutlineStar>}
                {loggedIn && isFavourite && <AiFillStar></AiFillStar>}
            </div>
            <div className="preview__picture"></div>
            <div className="preview__description__container">
                <div className="preview__title">{pharmacy.name}</div>
                <div className="preview__description">{pharmacy.address}</div>
                <div className="preview__description">{pharmacy.phone_number}</div>
                <div className="preview__description">{pharmacy.description}</div>
                <div className="preview__button" onClick={() => openDrugs(true)}>Show Drugs</div>
            </div>
        </div>
    )
}

export default Sidebar;