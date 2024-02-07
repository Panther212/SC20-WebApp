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

col1, col2 = st.columns([2,2])

with col1:
 labels = ['Plot 1','Plot 2','Plot 3','Plot 4']
 values = [24, 22, 26, 28]

 fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
 fig.update_layout(
    title="Infestation Overview",
    width=500,
    height=500,
 )
 st.plotly_chart(fig,use_container_width=True)

with col2:
 fig = go.Figure()
 fig.add_trace(go.Scatter(x=['Jan', 'Feb', 'March', 'April', 'May','June'], y=[20, 40, 25, 10,50,35], fill='tozeroy',mode='none',name='Plot 1')) # fill down to xaxis
 fig.add_trace(go.Scatter(x=['Jan', 'Feb', 'March', 'April', 'May','June'], y=[40, 60, 10, 40,25,60], fill='tonexty',mode='none',name='Plot 2')) # fill to trace0 y
 fig.update_layout(
    title="6 Months Data",
    xaxis_title="Month",
    yaxis_title="Percentage Infestation",
    width=500,
    height=500,
 )
 st.plotly_chart(fig,use_container_width=True)

