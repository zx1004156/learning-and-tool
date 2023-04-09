import requests
from pytube import YouTube

# 輸入YouTube影片網址
url = input("https://www.youtube.com/watch?v=a9__D53WsUs&ab_channel=AmazonWebServices")

# 下載YouTube影片
yt = YouTube(url)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download()
print("下載完成！")