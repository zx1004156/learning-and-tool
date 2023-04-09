from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import win32com.client
import os
import time
import pyautogui
from datetime import datetime,timedelta
from openpyxl import load_workbook
import pyautogui
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


chrome=''
def run_webdriver():
    global chrome
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument('--start-maximized')

    chrome = webdriver.Chrome("F:\\Python(Git)\\Python_Project\\爬蟲\\chromedriver.exe",chrome_options=options)
    chrome.get("")
    account = chrome.find_elements(By.XPATH,'//*[@id="account"]')[0]
    account.send_keys("")

    pw = chrome.find_elements(By.XPATH,'//*[@id="passwd"]')[0]
    pw.send_keys("")

    click1 = chrome.find_element(By.XPATH,'//*[@id="send"]')
    click1.click()#送驗證碼

    os.system(r"start C:\Users\user\Documents\Outlook")
    time.sleep(5)

    # 最大化当前窗口
    pyautogui.hotkey('win', 'up')
    
    # 移動滑鼠到指定位置
    pyautogui.moveTo(x=1603, y=133, duration=0.25)

    # 模擬滑鼠左鍵點擊
    pyautogui.click(button='left')
    time.sleep(5)
    
    #關掉oulook信箱
    pyautogui.hotkey('alt', 'F4')
    time.sleep(1)

    verification = chrome.find_elements(By.XPATH,'//*[@id="confirm_code"]')[0]
    verification.send_keys(read_outlook_mailbox())#填入驗證碼
    time.sleep(1)
    
    login = chrome.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/div/form/a')
    login.click()#登入鍵

    time.sleep(2)

    click2 = chrome.find_element(By.XPATH,'//*[@id="accordionSidebar"]/li[2]/a')
    click2.click()#左側幣別管理
    
    click3 = chrome.find_element(By.XPATH,'//*[@id="ftype"]/option[2]')
    click3.click() #下拉選單，身分選商家
    time.sleep(2)

    total = {}

    #選商家匯出excel
    for i in range(2,15):
        if i ==3:
            continue
        click4 = chrome.find_element(By.XPATH,'//*[@id="ftarget"]/option['+str(i)+']')
        click4.click() #商家選擇
        #*[@id="ftarget"]/option[2]
        #*[@id="ftarget"]/option[14]
        text = click4.text#取出商家名稱
        print(text)
    
        date_time_start = '23/02/01'
        date_time_end = '23/02/28'

        date_time_obj1 = datetime.strptime(date_time_start, '%y/%m/%d')
        start_date = str(date_time_obj1)[0:10]

        date_time_obj2 = datetime.strptime(date_time_end, '%y/%m/%d')
        end_date = str(date_time_obj2)[0:10]

        date1 = chrome.find_elements(By.XPATH,'//*[@id="fsdate"]')[0]
        date1.send_keys(start_date)

        date2 = chrome.find_elements(By.XPATH,'//*[@id="fedate"]')[0]
        date2.send_keys(end_date)

        click5 = chrome.find_element(By.XPATH,'//*[@id="fstatus"]/option[2]')
        click5.click()#已請款

        click6 = chrome.find_element(By.XPATH,'//*[@id="currency"]/option[2]')
        click6.click()#信東幣   

        click7 = chrome.find_element(By.XPATH,'//*[@id="search_btn"]')
        click7.click()#查詢
                
        time.sleep(2)

        click8 = chrome.find_element(By.XPATH,'//*[@id="example_wrapper"]/div[1]/button[2]')
        click8.click()#匯出excel
        time.sleep(3)

        os.rename(r'C:\Users\user\Downloads\請款資料表.xlsx',r'C:\Users\user\Downloads\\'+text+r".xlsx")

        time.sleep(10)

        date1.clear()
        date2.clear()

        #讀取excel檔
        mywb = load_workbook(r'C:\Users\user\Downloads\\'+text+r".xlsx")
        #更改excel欄位A1的標題名稱
        sheet = mywb['Sheet1']
        sheet['A1'] = text

        t = 3#從G3開始加總
        sum = 0#總和
        #加總G3 G4 G5...直到欄位為None為止
        while(sheet['G'+str(t)].value!=None):
            sum+=int(sheet['G'+str(t)].value)
            t+=1
        sheet['G'+str(t)] = sum    
        #存檔
        mywb.save(r'C:\Users\user\Downloads\\'+text+r".xlsx")

        total[text] = sum
        print(total)

        date1.clear()
        date2.clear()



#讀取outlook信件
def read_outlook_mailbox():
    account = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')
    
    inbox = account.Folders("C110003@sintong.com").Folders("信東APP驗證碼")  # 数字6代表收件箱
    mails = inbox.Items
    mails_count = 2
    mails.Sort('[ReceivedTime]', True) 
    for index in range(1, mails_count):
        mail = mails.Item(index)
        num = mail.body[-5:]
    return num

if __name__ == '__main__':
    run_webdriver()