import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/models/parkinsons_model.sav', 'rb'))

# Set page configuration
st.set_page_config(page_title="Disease Detection System (DDS)",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# Begin defining the sidebar
with st.sidebar:
    # Define a list of disease categories with their corresponding icons
    diseases = [
        ("Diabetes", "activity"),
        ("Heart Disease", "heart"),
        ("Parkinsons", "person")
    ]
    
    # Extract the disease names and icons into separate lists
    disease_names, disease_icons = zip(*diseases)

    # Create an option menu in the sidebar with the title 'Disease Detection System (DDS)'
    # The menu will dynamically populate with options and icons defined above
    selected = option_menu(
        'DDS',
        list(disease_names),
        menu_icon='hospital-fill',
        icons=list(disease_icons),
        default_index=0  # Set the first item as the default selection
    )
    
# Diabetes Prediction Page
if selected == 'Diabetes':
    # Page title
    st.title('Diabetes Prediction')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        glucose = st.text_input('Glucose Level')

    with col3:
        blood_pressure = st.text_input('Blood Pressure value')

    with col1:
        skin_thickness = st.text_input('Skin Thickness value')

    with col2:
        insulin = st.text_input('Insulin Level')

    with col3:
        bmi = st.text_input('BMI value')

    with col1:
        diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function value')

    with col2:
        age = st.text_input('Age of the Person')

    # Code for prediction
    diab_diagnosis = ''

    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin,
                      bmi, diabetes_pedigree_function, age]

        # Check if all inputs are filled
        if any(x.strip() == '' for x in user_input):
            st.error('Please fill in all fields to get a result.')
        else:
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                st.markdown("<p style='color:red;'>The person is diabetic. 😢</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='color:green;'>The person is not diabetic. 😌</p>", unsafe_allow_html=True)


# Heart Disease Prediction Page
if selected == 'Heart Disease':

    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'


# Parkinson's Prediction Page
if selected == "Parkinsons":

    # page title
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"