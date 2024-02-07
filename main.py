import streamlit as st
import numpy as np
import google.cloud
from google.cloud import firestore
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("testdata1-20ec5-firebase-adminsdk-an9r6-d15c118c96.json")
 
# Create a reference to the Google post.
doc_ref = db.collection("ScanData").document("5aXKu2fWBVm3OwR7rxnS")
 
# Then get the data at that reference.
doc = doc_ref.get()
 
# Let's see what we got!
#st.write("The id is: ", doc.id)
#st.write("The contents are: ", doc.to_dict())

col1, col2 = st.columns(2)

with col1:
 labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
 values = [4500, 2500, 1053, 500]

 fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
 st.plotly_chart(fig,width=800,height=400)

with col2:
 df = pd.DataFrame({
 'x': ['Jan', 'Feb', 'March', 'April', 'May'], 'y': [10,20,30,40,50]
 })

# Create a line chart with area under the curve
st.area_chart(df, x='x', y='y')


