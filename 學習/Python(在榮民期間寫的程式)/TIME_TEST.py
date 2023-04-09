from datetime import date
today = date.today()
s = date.strftime(today,'%Y-%m-%d %H:%M:%S')
m = s[5]+s[6]
d = s[8]+s[9]

if(m == '12' and d =='30'):
    print(m+' '+d)

