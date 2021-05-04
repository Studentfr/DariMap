import React, {useEffect} from 'react'
import Sidebar from "./Components/Sidebar/Sidebar";
import Map from "./Components/Map/Map";
import DrugSearch from "./Components/Sidebar/DrugSearch";

function App() {

    const [pharmacies, setPharmacies] = React.useState([])
    const [pharmacyId, setPharmacyId] = React.useState(0)
    const [previewVisibility, setPreviewVisibility] = React.useState(false)
    const [drugVisibility, setDrugVisibility] = React.useState(false)

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
    }, [])

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

    return (
        <div>
            <DrugSearch id={pharmacyId} isVisible={drugVisibility} closeDrugDescription={setDrugVisibility}/>
            <Sidebar id={pharmacyId} isVisible={previewVisibility} closeDescription={setPreviewVisibility} openDrugs={setDrugVisibility} />
            <Map pharmacies={pharmacies} onPharmacySelect={getSelectedPharmacyId}/>
        </div>
    )
}

export default App;
