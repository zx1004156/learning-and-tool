import requests

#抓取api
r = requests.get('https://api.thecatapi.com/v1/images/search')
data = r.json()
data2 = data[0]
data3 = data2['url']
print(data3)