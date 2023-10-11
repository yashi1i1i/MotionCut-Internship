from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://en.wikipedia.org/wiki/List_of_songs_by_Taylor_Swift"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
df=pd.read_html(str(table))
df=pd.DataFrame(df[1])
print(df)
data=df.drop(["Writer(s)","Ref.",],axis=1)

data.to_csv("WrittenByTaylorSwift.csv")
