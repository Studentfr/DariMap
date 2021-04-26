import React, {useEffect} from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'

function App() {

    const [mapConfig, setMapConfig] = React.useState({
        center: [54.8732, 69.1505],
        zoom: 13,
        scrollWheelZoom: true
    })

    const [pharmacies, setPharmacies] = React.useState([])

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

    /*const [todos, setTodos] = React.useState([])
    const [loading, setLoading] = React.useState(true)

    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/todos?_limit=5')
            .then(response => response.json())
            .then(todos => {
                setTimeout(() => {
                    setTodos(todos)
                    setLoading(false)
                }, 2000)
            })
    }, [])

    function toggleTodo(id) {
        setTodos(todos.map(todo => {
            if (todo.id === id) {
                todo.completed = !todo.completed
            }
            return todo
        }))
    }

    function removeTodo(id) {
        setTodos(todos.filter(todo => todo.id !== id))
    }

    function addTodo(title) {
        setTodos(todos.concat([{
            title,
            id: Date.now(),
            completed: false
        }]))
    }*/

    /*return (
        <Context.Provider value={{removeTodo}}>
            <div className="wrapper">
                <h1>React tutorial</h1>
                <Modal/>

                <React.Suspense fallback={<p>Loading...</p>}>
                    <AddTodo onCreate={addTodo}/>
                </React.Suspense>

                {loading && <Loader/>}
                {todos.length ?
                    (<TodoList todos={todos} onToggle={toggleTodo} />) :
                    (loading ? null : <p>No todos</p>)
                }

            </div>
        </Context.Provider>
    )*/

    const styles = {
        mapContainer: {
            height: "100vh"
        }
    }

    return (
        <MapContainer style={styles.mapContainer} center={mapConfig.center} zoom={mapConfig.zoom} scrollWheelZoom={mapConfig.scrollWheelZoom}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            {pharmacies.map((store) => {
                return (
                    <Marker position={[store.coordinate_id.latitude, store.coordinate_id.longitude]}
                            key={store.id}
                            eventHandlers={{
                                click: () => {

                                },
                            }}
                    >
                        <Popup>
                            <strong>{store.name}</strong>
                        </Popup>
                    </Marker>
                )
            })}
        </MapContainer>
    )
}

export default App;
