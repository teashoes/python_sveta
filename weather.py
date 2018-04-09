import requests
def get_html(url):
    res=requests.get(url)
    if res.status_code==200:
        print(res.text)
        # return res.json() #['name'] #json converts into dictionary
    else:
        print('woops')
if __name__ == '__main__':
    data = get_r('http://www.zakupki.gov.ru/epz/orderplan/quicksearch/search.html?
        searchString=%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%BE%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5
        &morphology=on
        &searchType=false
        &fz44=on
        &fz223=on
        &regions=
        &actualPeriodStart=01.01.2017
        &actualPeriodEnd=31.12.2017&publishDateFrom=&publishDateTo=&structured=true&sortBy=BY_MODIFY_DATE
        &pageNumber=1&sortDirection=false&recordsPerPage=_10')
# data=get_w("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=6710b438654f51bbf36d184f136cee7a&units=metric")
    print(data)