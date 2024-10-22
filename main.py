import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# st.title("Hello World")


st.header("Hello World")
# st.subheader("This is a subheader")
st.write("This is a simple text")

df = pd.DataFrame({
    "name": ["John", "Jane", "Doe"],
    "age": [25, 30, 35],
    "occupation": ["Data Scientist", "Data Analyst", "Data Engineer"]
})
st.dataframe(df)

editable_df = st.data_editor(df)

st.table(df)




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
    np.random.randn(1000, 2) / [50, 50] + [53.26530, 10.01310],
    columns=["lat", "lon"]
)
st.map(map_data)