import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import json
import pygeohash as pgh


# Setup Firebase
cred = credentials.Certificate(
    'certificate.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
print("Firebase Completed!")

# Setup file
with open('data-sample.json') as f:
    data = json.load(f)
print("File opened!")


for location in data:
    doc_ref = db.collection('elements').document()
    loc = [location['l'][0], location['l'][1]]
    doc_ref.set({
        "g": location['g'],
        "l": loc
    })
    print('Element uploaded')
