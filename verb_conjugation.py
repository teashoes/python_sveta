from bs4 import BeautifulSoup 
import requests

def get_html(url):
   res=requests.get(url)
   return res.text

def get_conj_1(verb):
    g_info = get_html('https://cooljugator.com/nl/'+verb)
    gen_info_p = BeautifulSoup(g_info, 'html.parser')
    conj_verb = gen_info_p.find_all(class_="meta-form")

    verbs_list = []
    for v in conj_verb:
        verbs_list.append(v.text)
    
    pronouns_list = []

    pronoun = gen_info_p.find_all(class_="ui ribbon label blue conjugation-pronoun")
    for pr in pronoun:
        pronouns_list.append(pr.text)

    return verbs_list, pronouns_list

print(get_conj('komen'))


# verb = input()
# g_info = get_html('https://cooljugator.com/nl/'+verb)
# gen_info_p = BeautifulSoup(g_info, 'html.parser')
# conjucation_dict = {}
# # conj_verb = gen_info_p.find_all(class_="meta-form")

# verbs_list = []

# for verb in conj_verb:
#     verbs_list.append(verb.text)
# print(verbs_list)
# # populate pronouns list
# pronouns_list = []
# # pronoun = gen_info_p.find_all(class_="ui ribbon label blue conjugation-pronoun")
# for pr in pronoun:
#     pronouns_list.append(pr.text)

# ######## 1.ДЕКАРТОВО ПРОИЗВЕДЕНИЕ НАДО СДЕЛАТЬ
# pronouns_list=pronouns_list[0:6]
# print(pronouns_list)
# ik = [True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False,
#     True, False,False,False,False,False]

# for i in pronouns_list:
#     for j in verbs_list:
#         conjucation_dict[i]=j
