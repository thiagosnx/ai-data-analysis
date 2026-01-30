import os 
import pymysql
from dotenv import load_dotenv
from infra.conn_provider import ConnProvider

load_dotenv()

class MySQLConnect(ConnProvider):
    def get_conn(self):
        conn = pymysql.connect(
            host=os.getenv("PORTGEN_HOST"),
            user=os.getenv("PORTGEN_USER"),
            database=os.getenv("PORTGEN_DB"),
            password=os.getenv("PORTGEN_PWD"),
            port=int(os.getenv("PORTGEN_PORT")),
        )
        return conn
        
