from bs4 import BeautifulSoup 
import requests

def get_html(url):
    res=requests.get(url)
    return res.text

srch = get_html('http://www.zakupki.gov.ru/epz/orderplan/plan-graph-card/search-position.html?revision-id=1737533')
g_info = get_html('http://www.zakupki.gov.ru/epz/orderplan/plan-graph-card/general-information.html?revision-id=1737533')

g_info_pars = BeautifulSoup(g_info, 'html.parser')
srch_p = BeautifulSoup(srch, 'html.parser')
#titles on the site
srch_list = srch_p.select('div.contentTabs span.td-content')
g_info_list = g_info_pars.select('div.noticeTabBoxWrapper tr')

# print(a_list)

# for title in srch_list:
    # print(title.text)
    # if a.text and a.text[0] == '№':
    #     print(a.text, a['href'])
for g_info_tite in g_info_list:
    print(g_info_tite.get_text())
# # print(lot_info)
# link=a['href']




