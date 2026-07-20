import streamlit as st

st.header("Chatbot")

if "count" not in st.session_state:
    st.session_state.count = 0

st.write(f"Current count {st.session_state.count}")

if st.button("Increase"):
    st.session_state.count+=1

if st.button("Decrease"):
    st.session_state.count-=1

if st.button("Reset"):
    st.session_state.countt =0

st.write(f"Updated count{st.session_state.count}")