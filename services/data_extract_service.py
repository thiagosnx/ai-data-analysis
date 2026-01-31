import pandas as pd
import pandas_gbq as pbq
from infra.bigquery_conn import BigQueryConnection
from infra.mysql_conn import MySQLConnect

class DataExtractService:
	def __init__(self):
		pass

	def extract_data_mysql(self, query):
		self.query = query
		mysql = MySQLConnect()
		conn = mysql.get_conn()
		df = pd.read_sql(self.query, conn)
		conn.close()
		return df
	
	def extract_data_gbq(self, query, project_id):
		self.query = query
		self.project_id = project_id
		bq = BigQueryConnection()
		bq = bq.get_conn(json='config_gbq.json')
		df = pbq.read_gbq(
			self.query,
			project_id=self.project_id,
			dialect="standard"
		)
		return df

