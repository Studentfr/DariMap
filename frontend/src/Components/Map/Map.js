import React from 'react'
import {MapContainer, Marker, TileLayer, Tooltip} from "react-leaflet";

function Map(props) {

    const [mapConfig, setMapConfig] = React.useState({
        center: [54.8732, 69.1505],
        zoom: 13,
        scrollWheelZoom: true
    })

    const styles = {
        mapContainer: {
            height: "100vh"
        }
    }

    const showDescription = (id) => {
        props.onPharmacySelect(id)
    }

    return (
        <MapContainer style={styles.mapContainer} center={mapConfig.center} zoom={mapConfig.zoom} scrollWheelZoom={mapConfig.scrollWheelZoom} zoomControl={false}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {props.pharmacies.map((store) => {
                return (
                    <Marker position={[store.coordinate_id.latitude, store.coordinate_id.longitude]}
                            key={store.id}
                            eventHandlers={{ click: () => showDescription(store.id) }}
                    >
                        <Tooltip>{store.name}</Tooltip>
                    </Marker>
                )
            })}
        </MapContainer>
    )
}

export default Map