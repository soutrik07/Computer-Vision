import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
URL = ""
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': URL
})

ref = db.reference('Students')

data = {
    "xxxxxxx":
        {
            "name": "A",
            "department": "Computer Science and Engineering",
            "starting": 2021,
            "year": 2,
            "total attendance": X,
            "last attendance": "2023-04-18 00:54:34",
            "standing": "good"
        },
    "yyyyyyyy":
        {
            "name": "B",
            "department": "Computer Science and Engineering",
            "starting": 2021,
            "year": 2,
            "total attendance": Y,
            "last attendance": "2023-04-18 00:54:34",
            "standing": "good"
        },
    "zzzzzzzzz":
        {
            "name": "C",
            "department": "Computer Science and Engineering",
            "starting": 2021,
            "year": 2,
            "total attendance": Z,
            "last attendance": "2023-04-18 00:54:34",
            "standing": "good"
        },
}

for key, value in data.items():
    ref.child(key).set(value)

