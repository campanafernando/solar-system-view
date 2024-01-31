import streamlit as st
import pydeck as pdk
from app.planetary_controller import get_planetary_positions
import numpy as np

st.title('Planetary Position Finder')

latitude = st.number_input('Enter your latitude', value=-23.78922340560141)  
longitude = st.number_input('Enter your longitude', value=-68.94112448205884)

if st.button('Show Planetary Positions'):
    positions = get_planetary_positions(latitude, longitude)

    layers = []
    for position in positions:
        x = position['altitude'] * np.cos(np.radians(position['azimuth']))
        y = position['altitude'] * np.sin(np.radians(position['azimuth']))
        
        layer = pdk.Layer(
            "TextLayer",
            data=[{'position': [longitude + y/100, latitude + x/100], 'text': position['name']}],
            get_size=16,
            get_color=[255, 255, 255],
            get_angle=0,
            get_text_anchor="'middle'",
            get_alignment_baseline="'center'"
        )
        layers.append(layer)

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=latitude,
            longitude=longitude,
            zoom=400,
            pitch=0,
        ),
        layers=layers
    ))
