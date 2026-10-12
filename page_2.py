import streamlit as st

st.title("Page 2")
st.write("Session state value for 'unit':", st.session_state.get("unit"))

if st.button("Switch to Page 1 via st.switch_page"):
    st.switch_page("page_1.py")
