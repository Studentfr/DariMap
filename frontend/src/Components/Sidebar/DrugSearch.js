import React, {useEffect} from "react";
import {AiFillCloseCircle} from "react-icons/ai";
import "./DrugSearch.css"

function DrugSearch({id, isVisible, closeDrugDescription}) {
    const [drugList, setDrugList] = React.useState([])
    const [searchString, setSearchString] = React.useState("")

    useEffect(() => {
        fetch(`api/drug-search/custom/?pharmacy_id=${id}&search=${searchString}`)
            .then(response => response.json())
            .then((drugList) => {
                setDrugList(drugList)
            },
            (error) => {
                console.log(error)
            })
    }, [searchString, id])

    const handleChange = (e) => {
        setSearchString(e.target.value)
    }

    return (
        <div className={`drug__container drug__container--${isVisible && id && "active"}`}>
            <div className="drug__close" onClick={() => closeDrugDescription(false)}>
                <AiFillCloseCircle></AiFillCloseCircle>
            </div>
            <div className="drug__description__container">
                <div className="drug__title">Drug List</div>

                <div className="relative">
                    <div
                        className="absolute top-0 left-0 h-full w-8 flex justify-center items-center"
                    >
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            className="h-4 w-4"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                clip-rule="evenodd"
                            />
                        </svg>
                    </div>
                    <input
                        type="text"
                        className="h-8 w-56 py-2 font-medium text-xs pr-9 pl-8 rounded-sm placeholder-gray-400 focus:outline-none"
                        placeholder="Search text..."
                        onChange={handleChange}
                    />
                </div>


                {drugList.map((drug) => {
                    return (

                        <div
                            className="bg-gray-100 mt-3 pl-3 border-green-300 dark:bg-gray-800 bg-opacity-95 border-opacity-60
                            | border-solid rounded-1xl border-2 | flex cursor-pointer
                            | hover:bg-green-400 dark:hover:bg-indigo-600 hover:border-transparent
                            | transition-colors duration-500">
                            <div className="flex flex-col justify-center">
                                <div>
                                    <p className="text-gray-900 dark:text-gray-300 font-semibold"><u>{drug.drug_id.name}</u></p>
                                </div>
                                <div>
                                    <p className="text-black dark:text-gray-100 text-justify font-semibold">Price: {drug.price} ₸</p>
                                    <p className=" text-black dark:text-gray-100 text-justify font-semibold">Amount: {drug.amount}</p>
                                </div>
                            </div>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

export default DrugSearch