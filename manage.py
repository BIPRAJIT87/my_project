import streamlit as st

st.title("      College First Year Students Details Form    ")
name= st.text_input("Enter Your Name :")
gname = st.text_input("Enter Gurdian Name :")
adr = st.text_area("Enter Your Address : ")
Year=st.selectbox("Enter Your Study Year :",(1,2,3,4))
Semester = st.selectbox("Enter Your Sem :",(1,2,3,4,5,6,7,8))

button = st.button("Submit")
if button :
    st.markdown(f""" 
    Name : {name}

    Gurdian Name : {gname}

    address : {adr}

    Year: {Year}

    Sem : {Semester} """)