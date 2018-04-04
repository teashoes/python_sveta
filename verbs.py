from bs4 import BeautifulSoup 
import requests
def get_html(url):
   res=requests.get(url)
   return res.text

def verb_conj(verb):
    g_info = get_html('https://cooljugator.com/nl/'+verb)
    gen_info_p = BeautifulSoup(g_info, 'html.parser')
    conj_verb = gen_info_p.find_all(class_="meta-form")
    pronoun = gen_info_p.find_all(class_="ui ribbon label blue conjugation-pronoun")

    verbs_list = []
    for verb in conj_verb:
            verbs_list.append(verb.text)

    pronouns_list = []
    for pr in pronoun:
        pronouns_list.append(pr.text)
    pronouns_list=pronouns_list[0:6]
    
    d=[]
    for i in range(0, 42, 6):
        d.append(dict(zip(pronouns_list,verbs_list[i:i+6])))

    return d

# a=verb_conj('komen')
# print(a[0])
