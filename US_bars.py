
import streamlit as st

# Bar properties in US customary units
bar_properties = {
    "#3": {"Diameter (in)": 0.375, "Area (in²)": 0.11, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 0.376},
    "#4": {"Diameter (in)": 0.5, "Area (in²)": 0.2, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 0.668},
    "#5": {"Diameter (in)": 0.625, "Area (in²)": 0.31, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 1.043},
    "#6": {"Diameter (in)": 0.75, "Area (in²)": 0.44, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 1.502},
    "#7": {"Diameter (in)": 0.875, "Area (in²)": 0.6, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 2.044},
    "#8": {"Diameter (in)": 1.0, "Area (in²)": 0.79, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 2.670},
    "#9": {"Diameter (in)": 1.128, "Area (in²)": 1.0, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 3.400},
    "#10": {"Diameter (in)": 1.27, "Area (in²)": 1.27, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 4.303},
    "#11": {"Diameter (in)": 1.41, "Area (in²)": 1.56, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 5.313},
    "#14": {"Diameter (in)": 1.693, "Area (in²)": 2.25, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 7.65},
    "#18": {"Diameter (in)": 2.257, "Area (in²)": 4.0, "Density (lb/in³)": 0.283, "Weight (lb/ft)": 13.6}
}

# Conversion factors
INCH_TO_MM = 25.4
IN2_TO_MM2 = 645.16
LB_IN3_TO_G_CM3 = 27.68
LB_FT_TO_KG_M = 1.48816

st.title("US Rebar Size Properties Viewer")

selected_bar = st.selectbox("Select Bar Size", list(bar_properties.keys()))
props = bar_properties[selected_bar]

# Display with metric units in parentheses
st.markdown(f"**Diameter:** {props['Diameter (in)']:.3f} in ({props['Diameter (in)'] * INCH_TO_MM:.2f} mm)")
st.markdown(f"**Area:** {props['Area (in²)']:.3f} in² ({props['Area (in²)'] * IN2_TO_MM2:.2f} mm²)")
st.markdown(f"**Density:** {props['Density (lb/in³)']:.3f} lb/in³ ({props['Density (lb/in³)'] * LB_IN3_TO_G_CM3:.2f} g/cm³)")
st.markdown(f"**Weight per Unit Length:** {props['Weight (lb/ft)']:.3f} lb/ft ({props['Weight (lb/ft)'] * LB_FT_TO_KG_M:.2f} kg/m)")
