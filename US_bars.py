
import tkinter as tk
from tkinter import ttk

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

def update_properties(event):
    selected_bar = bar_selector.get()
    props = bar_properties[selected_bar]

    diameter = props['Diameter (in)']
    area = props['Area (in²)']
    density = props['Density (lb/in³)']
    weight = props['Weight (lb/ft)']

    diameter_label.set(f"{diameter:.3f} in ({diameter * INCH_TO_MM:.2f} mm)")
    area_label.set(f"{area:.3f} in² ({area * IN2_TO_MM2:.2f} mm²)")
    density_label.set(f"{density:.3f} lb/in³ ({density * LB_IN3_TO_G_CM3:.2f} g/cm³)")
    weight_label.set(f"{weight:.3f} lb/ft ({weight * LB_FT_TO_KG_M:.2f} kg/m)")

root = tk.Tk()
root.title("US Bar Size Properties")

ttk.Label(root, text="Select Bar Size:").grid(column=0, row=0, padx=10, pady=10)
bar_selector = ttk.Combobox(root, values=list(bar_properties.keys()), state="readonly")
bar_selector.grid(column=1, row=0, padx=10, pady=10)
bar_selector.bind("<<ComboboxSelected>>", update_properties)

ttk.Label(root, text="Diameter:").grid(column=0, row=1)
diameter_label = tk.StringVar()
ttk.Label(root, textvariable=diameter_label).grid(column=1, row=1)

ttk.Label(root, text="Area:").grid(column=0, row=2)
area_label = tk.StringVar()
ttk.Label(root, textvariable=area_label).grid(column=1, row=2)

ttk.Label(root, text="Density:").grid(column=0, row=3)
density_label = tk.StringVar()
ttk.Label(root, textvariable=density_label).grid(column=1, row=3)

ttk.Label(root, text="Weight per Unit Length:").grid(column=0, row=4)
weight_label = tk.StringVar()
ttk.Label(root, textvariable=weight_label).grid(column=1, row=4)

root.mainloop()
