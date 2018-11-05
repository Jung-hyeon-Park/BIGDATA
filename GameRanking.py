import urllib.request
from pandas import DataFrame
from bs4 import BeautifulSoup

print("start")
i = 0
result = []
for i in range(8):
    site = "https://www.metacritic.com/browse/games/genre/date/action/vita?page="+str(i)

    hdr = {'User-Agent':'Mozilla/5.0', 'referer':'https://www.google.co.kr/'}

    req = urllib.request.Request(site, headers=hdr)

    response = urllib.request.urlopen(req)
    soup = BeautifulSoup(response, 'html.parser')

    tags = soup.findAll('div', attrs={'class':'basic_stat product_title'})
    tags2 = soup.findAll('div', attrs={'class':'metascore_w'})

    for tag, tag2 in zip(tags, tags2):
        print("%sㅣ%s\n"%(tag.text.strip(), tag2.text.strip()))
        result.append({'name':tag.text.strip(),'rank':tag2.text.strip()})

    i = i+1

rank_table = DataFrame(result, columns=('name','rank'))
rank_table.to_csv("game_rank_psVita.csv", encoding="utf-8", mode= 'w', index=False)

print("종료")