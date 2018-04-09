from bs4 import BeautifulSoup 
import requests
def get_html(url):
   res=requests.get(url)
   return res.text


#####do sth with pages
# for i in range(1, 3):
#     i=str(i)
#     b='%s?revision-id=1792779&okpd2IdsWithNested=on&okpd2Ids=8873901&page=%s&pageSize=50' % (core_site, i) 
#     plan_pages.append(b)

# print(plan_pages)

pos_html = get_html('http://zakupki.gov.ru/epz/orderplan/plan-graph-card/'
        'search-position-list.html?revision-id=1792779&okpd2IdsWithNested=on'
        '&okpd2Ids=8873901&page=1&pageSize=50')
pos_p = BeautifulSoup(pos_html, 'html.parser')
pos_num_p = pos_p.select('table tr')

#create dictionary
position_link={}
#collect links for zakupkas and zakupkas number on a particular page
i = 2
while i < len(pos_num_p):
    row_with_link = pos_num_p[i]
    row_with_id = pos_num_p[i + 1]
    i += 2
# collect links
    link = row_with_link.select('td div div ul li')[0]['onclick']
# populate dictionary
    linki=link[len('window.location=\''):-1]
    numberi=row_with_id.select('td')[0]['title']
    position_link[numberi] = linki
print(position_link)
