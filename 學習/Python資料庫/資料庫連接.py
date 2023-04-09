import pyodbc 
import tkinter as tk

server = 'DESKTOP-OLR65HM\SQLEXPRESS' 
database = 'Local_Database' 
username = '' 
password = '' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def update():
    rows = cursor.execute("update temp1 set 發幣名稱 = '春節禮' where 已領取金額 = '1500'")
    rows = cursor.execute("select * from temp1")
    for row in rows:
        print(row)
    cnxn.commit()
##############################################################################
'''
#視窗介面
window = tk.Tk()
window.title('Hello World')
window.geometry("300x100+250+150")

# 標示文字
label = tk.Label(window, text = '請輸入將搜尋的圖片內容')
label.pack()

# 輸入欄位
entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width = 20) # 輸入欄位的寬度
entry.pack()

# 按鈕
button = tk.Button(window, text = "OK", command = update)
button.pack()

window.mainloop()
'''