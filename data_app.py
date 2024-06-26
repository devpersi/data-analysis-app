import streamlit as st
from streamlit_navigation_bar import st_navbar
import os
import pages as pg

st.set_page_config(layout="wide",initial_sidebar_state="collapsed", page_title='data app', page_icon='img/ionianlogo.ico')

pages = ["Home", "2D Visualization", "Clustering Algorithms", "Classification Algorithms", "Algorithm Comparison", "Information", "GitHub"]
urls = {"GitHub":"https://github.com/kostasafe/data-analysis-app/"}
parent_dir = os.path.dirname(os.path.abspath("__file__"))
options = {
    "show_menu": False,
    "show_sidebar": False,
}

styles = {
    "nav": {
        "background-color": "#213a85",
        "justify-content": "center",
    },
    "div": {
        "max-width": "80rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "padding": "0.4375rem 0.625rem",
        "margin": "0 0.125rem",
    },
    "active": {
        "color": "var(--text-color)",
        "background-color": "black",
        "font-weight": "normal",
        "padding": "14px",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
functions = {
    "Home": pg.show_Home,
    "2D Visualization": pg.show_TwoD_Visualization,
    "Clustering Algorithms": pg.show_Clustering_Algorithms,
    "Classification Algorithms": pg.show_Classification_Algorithms,
    "Algorithm Comparison": pg.show_Comparison,
    "Information": pg.show_Info,
    #"GitHub" :pg.show_Git,
}

page = st_navbar(pages, styles=styles, urls=urls,options=options,)

go_to = functions.get(page)
if go_to:
    go_to()