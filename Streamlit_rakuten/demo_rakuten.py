import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st

#app.py
import app1
import app2
import app3
import app4



PAGES = {
    "Démarche": app4,
    "Dataviz reporting": app3,
    "Modélisation": app2,
    "Prédiction": app1
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
