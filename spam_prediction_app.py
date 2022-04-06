import streamlit as st
import joblib

model_1=joblib.load('spam_prediction')

st.title("EMAIL PREDICTION SYSTEM : SPAM OR HAM")
# user inputs
message = st.text_input("Enter your message that you want to predict")

# # predict the output
prediction = model_1.predict([message])

# #create a button , when press then output will predict
if st.button('PREDICT'):
  st.title(prediction[0])      #prints the output
print(prediction)