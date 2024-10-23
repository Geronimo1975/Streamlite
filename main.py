import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Lista de imagini
images = ['image1.jpeg', 'image2.jpeg', 'image3.jpeg'] 

st.title("Slideshow in Streamlit")

# Bucla pentru a itera prin imagini la fiecare 1.5 secunde
slide_placeholder = st.empty()  # Placeholder pentru imagini

for img in images:
    slide_placeholder.image(img)  # Afișează imaginea
    time.sleep(1.5)  # Pauză de 1.5 secunde înainte de următoarea imagine

st.title("Dynamic Streamlit Frontend")
st.header("Hello World")
st.write("This is a simple text")

df = pd.DataFrame({
    "name": ["John", "Jane", "Doe"],
    "age": [25, 30, 35],
    "occupation": ["Data Scientist", "Data Analyst", "Data Engineer"]
})


editable_df = st.data_editor(df)

# User interaction example
age_filter = st.slider("Select age range", 20, 40, (25, 35))
filtered_df = df[df['age'].between(*age_filter)]
st.dataframe(filtered_df)

# Plotting data
st.subheader("Age Distribution")
fig, ax = plt.subplots()
ax.bar(filtered_df['name'], filtered_df['age'])
st.pyplot(fig)


# st.markdown("This is a markdown")
# st.success("This is a success message")
# st.info("This is an info message")
#st.warning("This is a warning message")
# st.error("This is an error message")
# st.help()
st.divider()


st.image("https://www.python.org/static/img/python-logo.png", width=200)

st.image(os.path.join(os.getcwd(), "static", "GSC.jpg"))


st.subheader("Maps", "This is a map")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [100, 50] + [53.26530, 10.01310],
    columns=["lat", "lon"]
)
st.map(map_data)