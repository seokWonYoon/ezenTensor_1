from bs4 import BeautifulSoup
from urllib.request import urlopen
url = urlopen('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181124&charthour=10')
# lxml 패키지 설치
soup = BeautifulSoup(url, 'lxml')
# headers = {'User-Agent':'Chrome/66.0.3359.181'}
cnt_artist = 0
cnt_title = 0


for link1 in soup.find_all(name="p",attrs=({"class":"artist"})):
    cnt_artist += 1
    print(str(cnt_artist)+"위")
    print("아티스트 : " + link1.find('a').text)

print("----------------------------------------------------------------------------------")

for link2 in soup.find_all(name="p",attrs=({"class":"title"})):
    cnt_title += 1
    print(str(cnt_title)+"위")
    print("노래제목 : " + link2.text)
