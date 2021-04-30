#DariMap

##Drug
###['GET'] drug-list 
Gets all drugs

```
   {
      "id": 1,
      "name": "ibufen"
   },
   {
      "id": 2,
      "name": "paracetamol"
   }
```
###['GET'] drug-detail/1
Gets drug on a particular id

``
{
    "id": 1,
    "name": "ibufen"
}
``
###['POST'] drug-create
Creates a drug with consequent id

``
{
      "name": "aspirin"
}
``
###['POST'] drug-update/1
Updates drug on a particular id

``
{   
    "id" : "3",
    "name": "mask"
}
``
###['DELETE'] drug-delete/1
Deletes drug on a particular id

``
"Drug has deleted successfully"
``

##Pharmacy
###['GET'] pharmacy-list
Gets all pharmacies
```
[
    {
        "id": 1,
        "name": "Biosfera",
        "coordinate_id": {
            "latitude": 71.406717,
            "longitude": 51.172552
        }
    },
    {
        "id": 2,
        "name": "N54",
        "coordinate_id": {
            "latitude": 71.409336,
            "longitude": 51.160586
        }
    },
    {
        "id": 3,
        "name": "A-farm",
        "coordinate_id": {
            "latitude": 71.38255,
            "longitude": 51.144383
        }
    }
]
```
###['GET'] pharmacy-detail/1
Gets pharmacy on a particular id

```
{
    "Pharmacy": {
        "id": 1,
        "name": "Biosfera",
        "coordinate_id": {
            "latitude": 71.406717,
            "longitude": 51.172552
        }
    },
    "Coordinate": {
        "latitude": 71.406717,
        "longitude": 51.172552
    }
}
```
###['POST'] pharmacy-create
Creates a pharmacy with consequent id

``
{
      "name": "aspirin"
}
``
###['POST'] pharmacy-update/1
Updates pharmacy on a particular id

``
{   
    "id" : "3",
    "name": "mask"
}
``
###['DELETE'] pharmacy-delete/1
Deletes pharmacy on a particular id

``
"Pharmacy has deleted successfully"
``