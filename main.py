import streamlit as st
import numpy as np
import google.cloud
from google.cloud import firestore
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import pydeck as pdk
import calendar

st.set_page_config(layout="wide")
# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("testdata1-20ec5-firebase-adminsdk-an9r6-d15c118c96.json")
 
# Create a reference to the Google post.
doc_ref = db.collection("ScanData").document("5aXKu2fWBVm3OwR7rxnS")
 
# Then get the data at that reference.
doc = doc_ref.get()
 
# Let's see what we got!
#st.write("The id is: ", doc.id)
#st.write("The contents are: ", doc.to_dict())

Farmer_name= st.sidebar.header('Ramesh Kapare')

Farm_1 = st.sidebar.subheader('Niphad Farm')
Plot_1 = st.sidebar.write('Plot 15')
Plot_2 = st.sidebar.write('Plot 2')
Farm_2 = st.sidebar.subheader('Pimpalgaon Farm')
Plot_3 = st.sidebar.write('Plot 1')
# Convert the calendar data into a printable format
cal_rows = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
cal = calendar.monthcalendar(2024, 3)
for week in cal:
 cal_rows.append([str(day) if day != 0 else '' for day in week])
 
df = pd.DataFrame(cal_rows)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
#Display the calendar using Streamlit components
st.sidebar.dataframe(df,hide_index = True,width=500)
#st.write(cal_rows)
#st.dataframe(df)
#st.dataframe(df.style.hide(axis="index"))
#st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)


col1, col2 = st.columns([2,2])

with col1:
 labels = ['Plot 1','Plot 2','Plot 3','Plot 4']
 values = [24, 22, 26, 28]

 fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
 fig.update_layout(
    title="Infestation Overview",
    width=800,
    height=455,
    legend=dict(
    yanchor="bottom",
    y=0.01,
    xanchor="right",
    x=0.01)
 )
 st.plotly_chart(fig,use_container_width=True)
 st.image('Scans_Image.jpg',width=620)

with col2:
 fig = go.Figure()
 fig.add_trace(go.Scatter(x=['Jan', 'Feb', 'March', 'April', 'May','June'], y=[20, 40, 25, 10,50,35], fill='tozeroy',mode='none',name='Plot 1')) # fill down to xaxis
 fig.add_trace(go.Scatter(x=['Jan', 'Feb', 'March', 'April', 'May','June'], y=[40, 60, 10, 40,25,60], fill='tonexty',mode='none',name='Plot 2')) # fill to trace0 y
 fig.update_layout(
    title="6 Months Data",
    xaxis_title="Month",
    yaxis_title="Percentage Infestation",
    width=800,
    height=450,
 )
 st.plotly_chart(fig,use_container_width=True)

 chart_data = pd.DataFrame(
   np.random.randn(5, 1) / [60, 60] + [20.079966, 74.109314],
   columns=['lat', 'lon'])

 st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/satellite-streets-v12',
    initial_view_state=pdk.ViewState(
        latitude=20.079966,
        longitude=74.109314,
        zoom=13,
        pitch=50,
        height=450, width=600
    ),
    layers=[
     pdk.Layer(
            "ScreenGridLayer",
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[100, 30, 0, 160]',
            pickable=False,
            opacity=0.8,
            cell_size_pixels=20,
    #        color_range=[
    #         [0, 25, 0, 25],
     #        [0, 85, 0, 85],
     #        [0, 127, 0, 127],
     #        [0, 170, 0, 170],
     #        [0, 190, 0, 190],
     #        [0, 255, 0, 255],
      #        ],
         ),
    ],
 ))

