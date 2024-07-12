import streamlit as st

def app():
   st.markdown("""
    # CHIRAL Diseases Detection System (CHIRAL-DDS)
    By [Md. Jubayer Hossain](https://jhossain.netlify.app/)

    ### Objectives 
    This project aims to help doctors or medical professionals make data-driven decisions in health care, and they can easily detect patients with the disease. 
    
    ### Methodology
    The machine learning approach was used to develop this application. First, the datasets are obtained from public data sources like Kaggle. Then, preprocessing steps had done to clean data for better accuracy. Next, the mean imputes the missing values. Finally, the categorical features are encoded using the OneHot Encoding technique; all the steps were done by the Python machine learning library scikit-learn. 
    ### Refercences
    1. De S., Chakraborty B. (2020) Disease Detection System (DDS) Using Machine Learning Technique. In: Jain V., Chatterjee J. (eds) Machine Learning with Health Care Perspective. Learning and Analytics in Intelligent Systems, vol 13. Springer, Cham. https://doi.org/10.1007/978-3-030-40850-3_6
    2. Kalaiselvi K., Karthika D. (2020) Identifying Diseases and Diagnosis Using Machine Learning. In: Jain V., Chatterjee J. (eds) Machine Learning with Health Care Perspective. Learning and Analytics in Intelligent Systems, vol 13. Springer, Cham. https://doi.org/10.1007/978-3-030-40850-3_16
    """)
