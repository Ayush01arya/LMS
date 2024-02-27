import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Initialize Firebase
cred = credentials.Certificate('yu.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Streamlit UI
st.title('Laundry Management System')
import firebase_admin
from firebase_admin import credentials, firestore

# Path to your Firebase admin SDK JSON file
cred_path = 'yu.json'

# Initialize Firebase app if it hasn't been initialized yet
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Now you can get your Firestore client
db = firestore.client()

# Add laundry item
with st.form('add_laundry_form'):
    st.write('## Add Laundry Item')
    student_name = st.text_input('Student Name')
    cloth_item = st.text_input('Cloth Item')
    submit_button = st.form_submit_button('Submit')

    if submit_button:
        doc_ref = db.collection('laundry_items').document()
        doc_ref.set({
            'student_name': student_name,
            'cloth_item': cloth_item,
            'status': 'Submitted'
        })
        st.success('Laundry item added successfully!')

# View laundry items
st.write('## View Laundry Items')
docs = db.collection('laundry_items').stream()

# Creating a list to hold our data
data = []

for doc in docs:
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id
    data.append(doc_dict)

if data:
    df = pd.DataFrame(data)
    st.dataframe(df[['student_name', 'cloth_item', 'status']])
else:
    st.write("No laundry items found.")
