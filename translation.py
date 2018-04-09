from bs4 import BeautifulSoup 
import requests

def get_html(url):
   res=requests.get(url)
   return res.text

def get_trans(word):
    g_info = get_html('http://www.mijnwoordenboek.nl/vertaal/NL/EN/'+word)
    gen_info_p = BeautifulSoup(g_info, 'html.parser')
    a = gen_info_p.find_all('span', class_ = "deel4")
    word_list=[]
    for i in a:
        word_list.append(i.text)
    return word_list

# print(get_trans('boek'))