import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt
import warnings

dfTem = pd.read_excel('F:\\Python(Git)\\Python_Project\\學習\\tf44461500_win32.xltx',sheet_name = '資產')
#print(dfTem)
# 2019與2020的比較
df = dfTem.loc[2:8, ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']]
df = df.rename(columns={'Unnamed: 1': '流動資產','Unnamed: 2': '2019','Unnamed: 3': '2020'}) # 更改行 名稱
df =df.reset_index(drop=True)

#[]中括弧第一格都是列 第二格是行
#由於待會要做統計圖表，pandas函式內建的plot.bar()畫圖，這個函式不能顯示英文
df.at[0,'流動資產']= 'cash'
df.at[1,'流動資產']= 'investment'
df.at[2,'流動資產']= 'stock'
df.at[3,'流動資產']= 'AccountsReceivable'
df.at[4,'流動資產']= 'Prepayment'
df.at[5,'流動資產']= 'others'
df.at[6,'流動資產']= 'totalCurrentAssets'

#將Unnamed:流動資產列設置為索引，並替換掉原來的數字索引
try:
 df = df.set_index(dfTem.at[1, 'Unnamed: 1'])
 
except KeyError:
 print('你已經設定好index了')

ax = df.plot.bar(rot = 30) #rot=30可以讓x軸的標籤旋轉30度
plt.plot()
plt.tight_layout() # 這一行可以避免圖片的邊緣被白邊切到
plt.savefig("bar_plot.png") # 把圖片存成bar_plot.png
plt.show()

# 下面這兩行可以創建一個新的excel(images.xlsx)
workbook = xlsxwriter.Workbook('images.xlsx')
worksheet = workbook.add_worksheet()
# 把第一個欄位(A欄)延長，確定等一下要插入的文字不會看不清楚
worksheet.set_column('A:A', 30)
# 插入物件到excel的指定欄位
worksheet.write('A2', '圖片插入:') # 在A2插入 '圖片插入'四個字
worksheet.insert_image('B2', 'bar_plot.png') # 在B2插入我們做的bar_plot.png
# 編輯完了，把這個編譯器關掉
workbook.close()




print(df)