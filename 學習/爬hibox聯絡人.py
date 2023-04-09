import requests
from bs4 import BeautifulSoup

r = requests.get("https://apply.hibox.hinet.net/hiBox_extend/mailAdmin/index.php") #將網頁資料GET下來
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser

print(soup)

<option value="53f6afb97f2956b5">陸崇軒 &lt;aaronlu@sintong.com&gt;</option>
<option value="53f6afb97f2956b5">陸崇軒 &lt;aaronlu@sintong.com&gt;</option>
#member > option:nth-child(1)
document.querySelector("#member > option:nth-child(1)")

    color-scheme: dark !important;
    --darkreader-neutral-background: #131516;
    --darkreader-neutral-text: #d8d4cf;
    --darkreader-selection-background: #004daa;
    --darkreader-selection-text: #e8e6e3;
    border-collapse: collapse;
    border-spacing: 0;
    font: 99% arial,helvetica,clean,sans-serif;
    font-family: inherit;
    font-size: inherit;
    font-style: inherit;
    font-weight: inherit;

//*[@id="member"]/option[1]

/html/body/div/div[2]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr/td/div/dl/dd/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/select/option[1]