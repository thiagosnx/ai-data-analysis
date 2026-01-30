import streamlit as st


# from services.data_extract_service import DataExtractService 
from services.data_transformation_service import DataTransformationService 

data = DataTransformationService()
st.write(data.transformation_data_default())