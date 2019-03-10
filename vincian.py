from bs4 import BeautifulSoup
import requests
result=requests.get("https://vin01.tk/")
print(result)
src=result.content
soup=BeautifulSoup(src,'lxml')
company=[]
selects = soup.findAll('select')
for match in selects:
        match.decompose()
for categories in soup.div.center.find_all('a'):
        categories=categories.get_text()
        company.append(categories)
print(company)
