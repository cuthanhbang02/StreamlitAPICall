import streamlit as st 
import pandas as pd
import requests

token = ''

with st.form(key = "Login"):
    username = st.text_input("Username: ")
    password = st.text_input("Password: ", type="password")
    login_button = st.form_submit_button("Login")
if login_button:
    logged_in = requests.post("http://183.91.19.92:9092/api/Authenticate/login", json={"Username": username, "Password": password})
    if logged_in.json()['message']:
        st.error(logged_in.json()['message'])
    else:
        st.success("Login Successful")
        token = logged_in.json()['token']
        st.text(token)

with st.form(key = "RoomID"):
    roomid = st.text_input("Room ID:")
    getboard_button = st.form_submit_button("Submit")
if getboard_button:
    response = requests.get("http://183.91.19.92:9092/api/Procon/init-board?roomId=" + roomid)
    json_data = response.json()['data']
    df = pd.DataFrame(json_data)
    st.dataframe(df)


            
