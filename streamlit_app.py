import streamlit as st

with st.container(): 
    st.subheader('Hello!')
    st.write("---")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
             st.subheader("Meet ETA,")
             st.title('Your Assistant')
             st.write("##")
             st.write("______________________________________________")
             st.subheader(
                 """
                    ETA predicts heart attack risk based on reported symptoms.


                 """)

    with col2:
             st.markdown("![Alt Text](https://bit.ly/anna-find)")
             
           
