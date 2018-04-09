from bs4 import BeautifulSoup 
import requests
import re
import math

def get_html(url):
   res=requests.get(url)
   return res.text

pos_html = get_html('http://zakupki.gov.ru/epz/orderplan/plan-graph-card/'
        'search-position-list.html?revision-id=1792779&okpd2IdsWithNested=on'
        '&okpd2Ids=8873901&page=1&pageSize=50')

pos_p = BeautifulSoup(pos_html, 'html.parser')

cnt_pages_p = pos_p.select('div p.allRecords strong')[0]

cnt_pages=math.ceil(int(re.search(r'\d+', str(cnt_pages_p)).group())/50)
print(cnt_pages)
