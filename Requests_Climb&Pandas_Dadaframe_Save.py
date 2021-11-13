import requests
from bs4 import BeautifulSoup
import pandas as pd

#DataFrame 就是表格 ，columns就是欄位，欄位要帶list資料[]，不帶也可以可是欄位會沒有順序
#再將創出來的東西給到一個變數
df = pd.DataFrame(columns=['日文名稱','英文名稱','評分','部落格網址'])
url = 'https://tabelog.com/tw/osaka/rstLst/1/?SrtT=rt'
res = requests.get(url)
ans = BeautifulSoup(res.text)

rst = ans.find_all('li', class_='list-rst')
for i in rst:
    jp = i.find('small', class_='list-rst__name-ja').text
    point = i.find('b', class_='c-rating__val').text
    en = i.find('a', class_='list-rst__name-main').text
    blog = i.find('a', class_='list-rst__name-main')['href']
    print(jp,en,point,blog)
    #那每個表格都需要series(單行單列資料)，所以要創出series
    #記得裡面也是需要有[]中括弧
    #那index就是要去對上面的columns才不容易出錯!!引用順序可以不一樣，但是index順序要對 就不會出錯
    #最後再塞給一個變數!!
    s = pd.Series([jp,en,point,blog],index=['日文名稱','英文名稱','評分','部落格網址'])
    #最後一步就是把s塞進df裡面，ignore_index要設成True(因為她為自帶編號，True=把舊編號丟掉改成我定義的編號)
    #這是第一種專屬技能(複製一份新的後修改，舊的不動，所以要設定會去它才會修改)
    df = df.append(s, ignore_index=True)
#由於上面的df本身在迴圈外，那迴圈中有引入df，最後印出的df就會包括迴圈中的每一次操作!!
#.to_csv就是存檔的意思，tabelog.csv=檔案名稱，encoding不要忘記!!
# index它會自創自己的列編號 那我不需要 所以要false
df.to_csv("tabelog.csv", encoding='utf-8', index=False)