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

#a = 0#信東幣
#a = 1#盈養園幣

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
    time.sleep(3)
    
    #關掉oulook信箱
    pyautogui.hotkey('alt', 'F4')
    time.sleep(1)
   
   #填入驗證碼
    verification = chrome.find_elements(By.XPATH,'//*[@id="confirm_code"]')[0]
    verification.send_keys(read_outlook_mailbox())
    time.sleep(2)

    login = chrome.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/div/form/a')
    login.click()#登入

    click2 = chrome.find_element(By.XPATH,'//*[@id="accordionSidebar"]/li[2]/a')
    click2.click()#幣別管理

    click3 = chrome.find_element(By.XPATH,'//*[@id="ftype"]/option[2]')
    click3.click() #下拉選單商家

    time.sleep(2)

    click4 = chrome.find_element(By.XPATH,'//*[@id="ftarget"]/option[3]')
    click4.click() #商家選擇(選盈養園)


    a = 0#0是信東幣 1是盈養園幣
    d = 7#天數
    sintong_sum = 0
    yiyanyun_sum = 0
    while a<2:
        date_time_str = '23/03/16'
        date_time_obj = datetime.strptime(date_time_str, '%y/%m/%d')
        for i in range(d):       
            start_date = str(date_time_obj)[0:10]

            date1 = chrome.find_elements(By.XPATH,'//*[@id="fsdate"]')[0]
            date1.send_keys(start_date)

            date2 = chrome.find_elements(By.XPATH,'//*[@id="fedate"]')[0]
            date2.send_keys(start_date)

            click5 = chrome.find_element(By.XPATH,'//*[@id="fstatus"]/option[2]')
            click5.click()#已請款
            if a == 0:
                click6 = chrome.find_element(By.XPATH,'//*[@id="currency"]/option[2]')
                click6.click()#信東幣
            elif a== 1:
                click6 = chrome.find_element(By.XPATH,'//*[@id="currency"]/option[3]')
                click6.click()#盈養幣
            

            click7 = chrome.find_element(By.XPATH,'//*[@id="search_btn"]')
            click7.click()#查詢
            
            time.sleep(2)

            click8 = chrome.find_element(By.XPATH,'//*[@id="example_wrapper"]/div[1]/button[2]')
            click8.click()#匯出excel

            time.sleep(3)


            start_date2 = start_date.replace('-', '')
            #信東幣excel檔名改名
            if a == 0:
                dir = r"C:\Users\user\Downloads\盈養園(0986269079)請款資料表"+ start_date2 +r".xlsx"
            #盈養園幣excel檔名改名
            elif a == 1:
                dir = r"C:\Users\user\Downloads\盈養園(0986269079)請款資料表"+ start_date2 +r"_盈養園幣.xlsx"
            os.rename(r'C:\Users\user\Downloads\請款資料表.xlsx',dir)
            
            #讀取excel檔
            mywb = load_workbook(dir)
            #更改excel欄位A1的標題名稱
            sheet = mywb['Sheet1']
            if a == 0:
                sheet['A1'] = "盈養園(0986269079)請款資料表"+ start_date2
            elif a == 1:
                sheet['A1'] = "盈養園(0986269079)請款資料表"+ start_date2+"_盈養園幣"
            
            t = 3#從G3開始加總
            sum = 0#總和
            #加總G3 G4 G5...直到欄位為None為止
            while(sheet['G'+str(t)].value!=None):
                sum+=int(sheet['G'+str(t)].value)
                t+=1
            sheet['G'+str(t)] = sum    
            #存檔
            mywb.save(dir)

            if a == 0:
                sintong_sum += sum
                print(sintong_sum)
            elif a== 1:
                yiyanyun_sum += sum
                print(yiyanyun_sum)
            
            date_time_obj = date_time_obj + timedelta(days=1)#再加一天
            date1.clear()
            date2.clear()
        a = a+1

  
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