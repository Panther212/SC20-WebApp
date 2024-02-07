import streamlit as st
import firebase_admin
from firebase_admin import credentials, db, firestore

 
# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("testdata1-20ec5-firebase-adminsdk-an9r6-d15c118c96.json")
 
# Create a reference to the Google post.
doc_ref = db.collection("ScanData").document("Radar_Rawdata")
 
# Then get the data at that reference.
doc = doc_ref.get()
 
# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())

