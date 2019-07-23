import Geohash

grocery_stores=[{
    "id":57,
    "name":"Shop-Fresh",
    "location":[-1.74889, 36.257441]
},
    {
        "id": 7,
        "name": "Cabengers",
        "location": [-1.7009, 36.00441]
    },

    {
        "id": 5,
        "name": "Bro-Colli",
        "location": [-1.21222, 35.12002]
    },

    {
        "id": 37,
        "name": "Ventura",
        "location": [-0.99575, 36.24123]
    },

    {
        "id": 57,
        "name": "Jimny",
        "location": [-1.74889, 35.95141]
    },
]

# store using geohash
geohashed_list=[]
for item in grocery_stores:
    geohashed_list.append(
    {
        "id":item["id"],
        "name":item["name"],
        "geohash":Geohash.encode(item["location"][0], item["location"][1])
    }
    )
print(geohashed_list)