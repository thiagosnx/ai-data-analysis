import streamlit as st

from services.data_extract_service import DataExtractService 

data = DataExtractService()
st.write(data.extract_data_default())