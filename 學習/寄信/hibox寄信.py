#準備訊息物件設定
#載入模組
import email.message
from email.mime.application import MIMEApplication
from datetime import datetime,timedelta
import smtplib

#建立訊息物件
msg=email.message.EmailMessage()
#利用物件建立基本設定

from_a=""
to_b= ["","","","",""]

msg["From"]=from_a
msg["To"]=to_b
msg["Subject"]="每日業績表原始檔"

now = datetime.now()
now = now -timedelta(days = 1)
now_str = now.strftime("%Y-%m-%d")
file_name = r""

#寄送郵件主要內容
#msg.set_content("測試郵件純文字內容") #純文字信件內容
msg.add_alternative("此為系統每日自動寄出之每日業績表原始檔",subtype="html") #HTML信件內容
part = MIMEApplication(open(file_name,'rb').read())
part.add_header('Content-Disposition', 'attachment', filename= now_str + r"")
msg.attach(part)



#連線到SMTP Sevver


acc=""
password=""

#可以從網路上找到主機名稱和連線埠
server=smtplib.SMTP("www.hibox.hinet.net",25) #建立
server.login(acc,password)
server.send_message(msg)
server.close() #發送完成後關閉連線

