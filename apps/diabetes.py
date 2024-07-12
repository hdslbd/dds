import streamlit as st

def app():
    st.markdown("""
    # CHIRAL-DDS: Diabetes Disease Detection
    By [Md. Jubayer Hossain](https://jhossain.netlify.app/)
    
    This project aims to help doctors or medical professionals make data-driven decisions in health care, and they can easily detect patients with the disease. 
    """)
    st.sidebar.write("""
    ## About Disease  
    ### Symptoms
    Symptoms goes here!  
    [Source: World Health Organization]()
    
    """)   

    st.write("""
    > **Please provide all the information below and click predict button.**
    """)

    st.number_input("Write the number of time patients pregnant")
    st.number_input("Write the value of Plasma glucose concentration a 2 hours in an oral glucose tolerance test of Patients")
    st.number_input("Write the value of Diastolic blood pressure(mmHg) of Patient" )
    if st.button("Predict"):
        st.write("""**Probably, you have diabetes!**""")
 

