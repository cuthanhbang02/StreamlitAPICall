import streamlit as st 
import pandas as pd
import requests

token = ''
roomid = ''
with st.form(key = "Login"):
    token = st.text_input("Token:")
    roomid = st.text_input("Room ID:")
    login_button = st.form_submit_button("Login")
if login_button:
    st.text(token)
    
    response = requests.get("http://183.91.19.92:9092/api/Procon/init-board?roomId=" + roomid)
    json_data = response.json()['data']
    df = pd.DataFrame(json_data)
    st.text("Room board")
    st.dataframe(df)
  
st.header("Craftment Action")
with st.form(key = "Move"):
    side = st.selectbox("Side", ["Green", "Red"])
    st.text("Craftment 0")
    c0actionname = st.selectbox("C0 Action Name", ["Move", "Build", "Destroy"])
    c0direction = st.selectbox("C0 Direction", ["Right", "Left", "Top", "Bottom"])
    st.text("Craftment 1")
    c1actionname = st.selectbox("C1 Action Name", ["Move", "Build", "Destroy"])
    c1direction = st.selectbox("C1 Direction", ["Right", "Left", "Top", "Bottom"])
    st.text("Craftment 2")
    c2actionname = st.selectbox("C2 Action Name", ["Move", "Build", "Destroy"])
    c2direction = st.selectbox("C2 Direction", ["Right", "Left", "Top", "Bottom"])
    st.text("Craftment 3")
    c3actionname = st.selectbox("C3 Action Name", ["Move", "Build", "Destroy"])
    c3direction = st.selectbox("C3 Direction", ["Right", "Left", "Top", "Bottom"])
    st.text("Craftment 4")
    c4actionname = st.selectbox("C4 Action Name", ["Move", "Build", "Destroy"])
    c4direction = st.selectbox("C4 Direction", ["Right", "Left", "Top", "Bottom"])
    move_button = st.form_submit_button("Submit")

if move_button:
    st.text(token)
    st.text(roomid)
    response = requests.post("http://183.91.19.92:9092/api/Procon/send-action", json= {
    "RoomId": roomid,
    "CraftmentActionList":[
        {
            "Id": side + "craftment0",
            "ActionName": c0actionname,
            "Direction": c0direction
        },
        {
            "Id": side + "craftment1",
            "ActionName": c1actionname,
            "Direction": c1direction
        },
        {
            "Id": side + "craftment2",
            "ActionName": c2actionname,
            "Direction": c2direction
        },
        {
            "Id": side + "craftment3",
            "ActionName": c3actionname,
            "Direction": c3direction
        },
        {
            "Id": side + "craftment4",
            "ActionName": c4actionname,
            "Direction": c4direction
        },
        
    ]    
}, headers = {
    "Authorization": "Bearer " + token
}
)
    st.text(response.json())

    status = response.json()
    df = pd.DataFrame(status['data'])
    st.dataframe(df)

            
