from bs4 import BeautifulSoup
import requests
result=requests.get("https://vin01.tk/")
print(result)
src=result.content
soup=BeautifulSoup(src,'lxml')
company=[]
selects = soup.findAll('font')
for match in selects:
        match.decompose()
for categories in soup.div.center.find_all('a'):
        categories=categories.get_text().strip()
        company.append(categories)
for letter in company:
        print(letter)
