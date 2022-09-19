from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.


app.config["MYSQL_HOST"]              = "127.0.0.1"
app.config["MYSQL_USER"]              = "root"
app.config["MYSQL_PASSWORD"]          = "1234"
app.config["MYSQL_DB"]                = "MIPSS_"
#app.config["MYSQL_PORT"]              = "3306"
#app.config["MYSQL_UNIX_SOCKET"]       = ""
#app.config["MYSQL_CONNECT_TIMEOUT"]   = ""
#app.config["MYSQL_READ_DEFAULT_FILE"] = ""
#app.config["MYSQL_USE_UNICODE"]       = ""
#app.config["MYSQL_CHARSET"]           = ""
#app.config["MYSQL_SQL_MODE"]          = ""
app.config["MYSQL_CURSORCLASS"]       = "DictCursor"

mysql = MySQL(app)