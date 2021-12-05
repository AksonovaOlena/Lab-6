import requests
from bs4 import BeautifulSoup
from lxml import html
from collections import Counter
from lxml import etree
import cssselect


link="https://www.ukr.net"
serviceNow_r=requests.get(link)
sNow_soup=BeautifulSoup(serviceNow_r.text, 'html.parser')

print(sNow_soup.find_all('href',{'class':'cta-list component'}))


for name in sNow_soup.find_all('href',{'class':'cta-list component'}):
    print(name.text)
 
link='https://www.ukr.net'
page=requests.get(link)
tree=html.fromstring(page.content)
 
elms=tree.cssselect('*')
tags=[x.tag for x in elms]
 
count=Counter(tags)
 
 
for e in count:
    print('{}: {}'.format(e, count[e]))
 
def img(link):
    resp=requests.get(link)
    pars=etree.HTMLParser()
    radical=etree.fromstring(resp.content, parser=pars)

    return int(radical.xpath('count(//img)'))
print(img('https://www.ukr.net'))
input()