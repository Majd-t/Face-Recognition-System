import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {

    'dataBaseURL':"https://face-recognition-a-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data ={
            "ahmed":
                        {
                        "T.C": "983724914",
                        "name": "Mecid temir",
                        "Nationality": "SY",
                        "old":23,
                        "murder": "E"
                        }
     }


for key ,value in data.items():
    ref.child(key).set(value)