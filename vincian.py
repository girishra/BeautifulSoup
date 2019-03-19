from bs4 import BeautifulSoup
import requests
import re
result=requests.get("https://vin01.tk/")
src=result.content
soup=BeautifulSoup(src,'lxml')
for tag in soup.div.center('a'):
    if tag.find('font'):
        f=tag.find('font')
        print(f.previousSibling)
    else:
        print(tag.text)
other=soup.find('div').text
c_companies=re.search('Few.*\n.*',other).group()
cc=re.findall('[A-Za-z]+.\w+,',c_companies)
for letter in cc:
    print(letter)
