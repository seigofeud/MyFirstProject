import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title("Streamlit 超入門")

st.write("Display Image")

img = Image.open("C:\Users\福岡　青梧\mypythonproject\MayuTamura.JPG")
st.image(img, caption="Mayu Tamura", use_column_width=True)

