import React, {useEffect} from 'react'
import { AiFillCloseCircle } from 'react-icons/ai';
import "./Sidebar.css"

function Sidebar({id, isVisible, closeDescription}) {
    let pharmacy = {}

    useEffect(() => {
        fetch(`api/pharmacy-detail/${id}`)
            .then(response => response.json())
            .then((result) => {
                pharmacy = result
            },
            (error) => {
                console.log(error)
            })
    }, [id])

    return(
        <div className={`preview__container preview__container--${isVisible && id && "active"}`}>
            <div className="preview__close" eventHandlers={{click: () => {closeDescription(false)}}}>
                <AiFillCloseCircle></AiFillCloseCircle>
            </div>
            <div className="preview__picture"></div>
            <div className="preview__description__container">
                <div className="preview__title">{pharmacy.name}</div>
            </div>
        </div>
    )
}

export default Sidebar;