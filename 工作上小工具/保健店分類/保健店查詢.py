import pyodbc
import pandas as pd
import datetime
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font
from tkinter import filedialog
import os

today = datetime.date.today()


# 建立連線字串
server = ''
database = ''
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'
cnxn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# 連線
cnxn = pyodbc.connect(cnxn_str)

# 建立游標
cursor = cnxn.cursor()

# 執行 SQL 查詢
query = """"""

cursor.execute(query)

# 取得查詢結果
result = cursor.fetchall()


df = pd.read_sql(query,cnxn)
# 將查詢結果轉換為 DataFrame
#desc[0] for desc in cursor.description

# 匯出到 Excel 檔案
filename = str(today)+"保健店消耗量(未分類).xlsx"
df.to_excel(filename, index=False)



file_path = filedialog.askopenfilename()
if not file_path:
    os._exit(0)
mywb = load_workbook(
    file_path)


#去除框線
Sheet = mywb['Sheet1']
for row in Sheet.rows:
    for cell in row:
        cell.border = openpyxl.styles.Border()
#改字體大小
font = Font(size=12)
for row in Sheet.rows:
    for cell in row:
        cell.font = font

mywb.save(filename)  # 另存新檔