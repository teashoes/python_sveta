from bs4 import BeautifulSoup 
import requests

def get_html(url):
   res=requests.get(url)
   return res.text

def get_art(noun):
    g_info = get_html('https://www.welklidwoord.nl/'+noun)
    gen_info_p = BeautifulSoup(g_info, 'html.parser')
    a = gen_info_p.find('span') 
    return a.text

# print(get_art('boek'))


