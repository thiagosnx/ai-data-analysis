import pandas as pd

from services.data_extract_service import DataExtractService

class DataTransformationService:
    def transformation_data_default(self):
        dt = DataExtractService()

        df = dt.extract_data_default()

        df = (
            df \
            .assign(
                nome=lambda x: x["nome"].str.title(),
                modelo=lambda x: x["nome_modelo"].str.title(),
                preco=lambda x: pd.to_numeric(x["preco"], errors="coerce")
            )
        )
        return df


