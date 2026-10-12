import streamlit as st

st.sidebar.checkbox("set unit to True", key="unit")

pg = st.navigation([
    st.Page("page_1.py", title="Page 1"),
    st.Page("page_2.py", title="Page 2")
])
pg.run()
