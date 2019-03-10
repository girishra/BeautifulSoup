1.from bs4 import BeautifulSoup
2.import requests
3.result=requests.get("https://vin01.tk/")
4.result
5.src=result.content
6.soup=BeautifulSoup(src,'lxml')
7.company=[]
8.selects = soup.findAll('select')
9.for match in selects:
        match.decompose()
10.for categories in soup.div.center.find_all('a'):
        categories=categories.get_text()
        company.append(categories)
11.company
