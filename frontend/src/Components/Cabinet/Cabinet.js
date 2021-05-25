import "./Cabinet.css"

function Cabinet() {
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


                        <div className="row">

                            <div className="cell" data-title="Pharmacies">
                                Биосфера
                            </div>
                            <div className="cell" data-title="Delete">
                                <button type="button" className="delete">Delete</button>
                            </div>

                        </div>

                        <div className="row">

                            <div className="cell" data-title="Pharmacies">
                                Центральная аптека
                            </div>
                            <div className="cell" data-title="Delete">
                                <button type="button" className="delete">Delete</button>
                            </div>
                        </div>

                        <div className="row">
                            <div className="cell" data-title="Pharmacies">
                                Инфо+
                            </div>
                            <div className="cell" data-title="Delete">
                                <button type="button" className="delete">Delete</button>
                            </div>
                        </div>


                    </div>
                </div>
            </div>
        </div>
    )
}

export default Cabinet
