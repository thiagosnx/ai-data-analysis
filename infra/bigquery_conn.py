import os 
from google.cloud import bigquery
from infra.conn_provider import ConnProvider

class BigQueryConnection(ConnProvider):
    def get_conn(self, json):
        self.json = json
        client = bigquery.Client.from_service_account_json(
            json
        )
        return client

