import streamlit as st

st.title("Page 1")
st.write("Session state value for 'unit':", st.session_state.get("unit"))
