import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtimeproject-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2021CSB104":
        {
            "name": "Soutrik Roy",
            "department": "Computer Science and Technology",
            "starting": 2021,
            "year": 2,
            "total attendance": 40,
            "last attendance": "2023-04-18 00:54:34",
            "standing": "good"
        },
    "2021CSB071":
        {
            "name": "Prayas Mazumder",
            "department": "Computer Science and Technology",
            "starting": 2021,
            "year": 2,
            "total attendance": 40,
            "last attendance": "2023-04-18 00:54:34",
            "standing": "good"
        },
    "2021CSB111":
        {
            "name": "Sumeet Soreng",
            "department": "Computer Science and Technology",
            "starting": 2021,
            "year": 2,
            "total attendance": 40,
            "last attendance": "2023-04-18 00:54:34",
            "standing": "good"
        },
}

for key, value in data.items():
    ref.child(key).set(value)

