from bs4 import BeautifulSoup 
import requests

def get_html(url):
    res=requests.get(url)
    return res.text

site_ = get_html(
    'http://www.zakupki.gov.ru/epz/orderplan/quicksearch/search.html'
    '?searchString=%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%BE%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5'
    '&morphology=on&searchType=false&fz44=on&fz223=on&regions=&actualPeriodStart=01.01.2017'
    '&actualPeriodEnd=31.12.2017&publishDateFrom=&publishDateTo=&structured=true'
    '&sortBy=BY_MODIFY_DATE&pageNumber=1&sortDirection=false&reordsPerPage=_10')
# print(site_)

bs = BeautifulSoup(site_, 'html.parser')

# a_list = bs.select('div.registerBox.registerBoxBank.margBtm20 table td.descriptTenderTd dt a')

# lot_info=[]

# for a in a_list:
#     print(a.text)
#     lot_name = lot.find('a[href]')
#     lot_info.append(lot_name.text)

for a in bs.select('a'):
    if a.text and a.text[0] == '№':
        print(a.text, a['href'])

# print(lot_info)
link=a['href']

# for a in a_list:
#     print(a.text)

