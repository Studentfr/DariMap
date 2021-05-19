import React, {useEffect} from 'react'
import { AiFillCloseCircle } from 'react-icons/ai';
import "./Sidebar.css"
import DrugSearch from "./DrugSearch";

function Sidebar({id, isVisible, closeDescription, openDrugs}) {
    const [pharmacy, setPharmacy] = React.useState({})

    useEffect(() => {
        fetch(`api/pharmacy-detail/${id}`)
            .then(response => response.json())
            .then((pharmacy) => {
                setPharmacy(pharmacy)
            },
            (error) => {
                console.log(error)
            })
    }, [id])

    return(
        <div className={`preview__container preview__container--${isVisible && id && "active"}`}>
            <div className="preview__close" onClick={() => closeDescription()}>
                <AiFillCloseCircle></AiFillCloseCircle>
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