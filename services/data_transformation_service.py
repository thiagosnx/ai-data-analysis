import pandas as pd

from services.data_extract_service import DataExtractService

class DataTransformationService:
    def transform_data_mysql(self):
        dt = DataExtractService()
        df = dt.extract_data_mysql()
        df = (
            df \
            .assign(
                nome=lambda x: x["nome"].str.split().str[0],
                email=lambda x: x["email"].str.replace(
                    r'(^.).*(@.*$)', 
                    r'\1****\2', 
                    regex=True
                ),
                matricula=lambda x: x["matricula"].str.replace(
                    r'.*(\d{2})$',
                    r'*******\1',
                    regex=True
                ),
                modelo=lambda x: x["nome_modelo"].str.title(),
                estado=lambda x: x["estado"].str.title(), # if not uf
                preco=lambda x: pd.to_numeric(x["preco"], errors="coerce"),
            )
        )
        return df


