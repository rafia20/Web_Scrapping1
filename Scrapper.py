import requests
from bs4 import BeautifulSoup

#getting data from website 
req=requests.get("https://www.geeksforgeeks.org/")


#using soup libaray to convert into html parser 
soup=BeautifulSoup(req.content,"html.parser")

#printing data 

print(soup.prettify())

res = soup.title

print(res.get_text())
