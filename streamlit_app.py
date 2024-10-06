import streamlit as st

st.set_page_config(page_title="ETA - Heart Attack Risk", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Predict", "Enter Predictions"))

# Home Page
if page == "Home":
    st.subheader("Hello!")
    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Meet ETA,")
        st.title('Your Assistant')
        st.write("##")
        st.write("______________________________________________")
        st.subheader("ETA predicts heart attack risk based on reported symptoms.")

    with col2:
        st.markdown("![Alt Text](https://bit.ly/anna-find)")

    st.write("---")

# Importing and displaying other pages based on navigation
if page == "Predict":
    import predict  # This will run the predict.py file

if page == "Enter Predictions":
    import enter_predictions  # This will run the enter_predictions.py file
