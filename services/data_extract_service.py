import pandas as pd
from infra.mysql_conn import MySQLConnect

class DataExtractService:
	def extract_data_default(self):
		conn = MySQLConnect()
		query = """
		select distinct
		p.matricula,
		p.nome ,
		p.email ,
		p.estado,
		m.nome_modelo, 
		m.preco,
		p.created_at 
		from portgen.portfolios p
		join pagamentos pg on pg.id = p.id_pgto
		join modelos m on m.id = p.id_modelo 
		where 1=1
		and pg.status = 'approved';
		"""
		df = pd.read_sql(query, conn.get_conn())

		conn.get_conn().close
		return df
