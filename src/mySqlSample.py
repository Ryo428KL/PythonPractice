# インポート MySQLdb
import MySQLdb

# 環境変数読み込み
from dotenv import load_dotenv
load_dotenv()
import os
useName = os.getenv('MYSQL_USER')
userPassword = os.getenv('MYSQL_PASSWORD')
dbName = os.getenv('MYSQL_DB')

# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
  host = 'localhost',
  user = useName,
  passwd = userPassword,
  db = dbName)
cursor = connection.cursor()

# SQL実行
cursor.execute('select * from table1')
rows = cursor.fetchall()
for row in rows:
  print(row)

# 接続を閉じる
connection.close()
