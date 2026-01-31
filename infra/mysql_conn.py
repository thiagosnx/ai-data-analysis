import os 
import pymysql
from dotenv import load_dotenv
from infra.conn_provider import ConnProvider

load_dotenv()

class MySQLConnect(ConnProvider):
    def get_conn(self):
        conn = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            database=os.getenv("MYSQL_DB"),
            password=os.getenv("MYSQL_PWD"),
            port=int(os.getenv("MYSQL_PORT")),
        )
        return conn
        
