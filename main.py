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
st.title('Farm Analytics')
# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("testdata1-20ec5-firebase-adminsdk-an9r6-d15c118c96.json")
 
# Create a reference to the Google post.
doc_ref = db.collection("ScanData").document("5aXKu2fWBVm3OwR7rxnS")
 
# Then get the data at that reference.
doc = doc_ref.get()
 
# Let's see what we got!
#st.write("The id is: ", doc.id)
#st.write("The contents are: ", doc.to_dict())
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #1b1a28;
    }
</style>
""", unsafe_allow_html=True)
Farmer_image = st.sidebar.image('WhatsApp Image 2024-02-09 at 21.25.12_60b97c05.jpg')
#Farmer_name= st.sidebar.header('Ramesh Kapare')
st.sidebar.markdown("<h1 style='text-align: center; color: white;font-size: 32px;'>Ramesh Kapare  </h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; color: white;font-size: 25px;'>Niphad Farm </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; color: #247370;font-size: 19px;'>Plot number 1 </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; color: #1a5361;font-size: 19px'>Plot number 2 </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; color: white;font-size: 25px;'>Pimpalgaon Farm </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; color: #31458a;font-size: 19px'>Plot number 3 </h2>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='text-align: center; color: #738fd9;font-size: 19px'>Plot number 4 </h2>", unsafe_allow_html=True)
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
 values = [28, 26, 24, 22]

 fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
 fig.update_layout(
    title="Infestation Overview",
    width=800,
    height=455,
    {
    ‘plot_bgcolor’: ‘rgba(0, 0, 0, 0)’,
    ‘paper_bgcolor’: ‘rgba(0, 0, 0, 0)’,
     },
    legend=dict(
    yanchor="bottom",
    y=0.01,
    xanchor="right",
    x=0.01)
 )
 colors = ['#4b4eb2', '#2fe2cc', '#1e5378', '#03d4fd']
 fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))

 st.plotly_chart(fig,use_container_width=True)
 #st.image('Scans_Image.jpg',width=620)
 Plots=['Plot 1', 'Plot 2']
 fig3 = go.Figure(data=[
    go.Bar(name='Healthy', x=Plots, y=[200, 180],marker_color='#3488a0'),
    go.Bar(name='Infected', x=Plots, y=[250, 150],marker_color='#773871'),
    go.Bar(name='Suspicious', x=Plots, y=[120, 180],marker_color='#25d9c4')
 ])
 fig3.update_layout(barmode='group',width=800,
    height=530,title='Comparative Analysis')
 st.plotly_chart(fig3,use_container_width=True)


with col2:
 fig = go.Figure()
 fig.add_trace(go.Scatter(x=['Jan', 'Feb', 'March', 'April', 'May','June'], y=[20, 40, 25, 15,10,40], fill='tozeroy',mode='none',name='Plot 1',line_shape='spline')) # fill down to xaxis
 fig.add_trace(go.Scatter(x=['Jan', 'Feb', 'March', 'April', 'May','June'], y=[10, 15, 20, 35,28,15], fill='tonexty',mode='none',name='Plot 2',line_shape='spline')) # fill to trace0 y
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
 st.markdown("<h2 style='text-align: left; color: white;font-size: 18px'>Overview </h2>", unsafe_allow_html=True)
 st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/satellite-streets-v12',
    initial_view_state=pdk.ViewState(
        latitude=20.079966,
        longitude=74.109314,
        zoom=13,
        pitch=50,
        height=430, width=600,
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

