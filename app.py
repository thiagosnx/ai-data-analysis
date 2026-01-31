import streamlit as st
import pandas as pd
import pandas_gbq as bq

from services.data_extract_service import DataExtractService 
from services.data_transformation_service import DataTransformationService 



# file = st.file_uploader(
#     "Escolha um arquivo",
#     type=["csv", "parquet", "xlsx"]
# )

from google.cloud import bigquery

client = bigquery.Client.from_service_account_json(
    "config.json"
)

query = """
    select distinct
        nome, 
        marca, 
        string_agg(tamanho, ', ' order by tamanho) as tamanhos,
        preco_atual, 
        preco_real
    from `eco-avenue-461519-f8.telegramdata.shops`
    where 1=1
    and preco_atual < preco_real
    and disponivel = 1
    group by 
        nome, 
        marca, 
        preco_atual, 
        preco_real
    order by preco_atual asc
"""

query_job = client.query(query)
rows = query_job.result()

df = bq.read_gbq(
    query,
    project_id="eco-avenue-461519-f8",
    dialect="standard"
)


# raw = DataExtractService(file)
# data = DataTransformationService()
# st.write(data.transformation_data_default(raw))
st.write(df)