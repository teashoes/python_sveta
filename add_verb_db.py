from database import db_session, Verb
from verbs import verb_conj
import csv

def verb_add(verb_name):
    for i in range(0,6,1):
        vv=verb_conj(verb_name)
        v=vv[i]
        for j in v.keys():
            verbadd=Verb(verbname=verb_name, tense_id = i, tense = 'NULL', pronoun =j, converb = v[j]) 
            db_session.add(verbadd)
    db_session.commit()    
# vvv=verb_add('komen')


if __name__ == "__main__":
    with open('verblist.csv', 'r', encoding='utf-8') as v_list:
        reader = csv.reader(v_list, delimiter=',', quotechar='"')
        # next(reader, None)  # skip the headers
        data_read=[]
        for i in reader:
            data_read.append(i)

    count = 0
    while (count < len(data_read)):
        verb_name_list=data_read[count]
        verb_name=verb_name_list[0]
        for i in range(0,6,1):
            vv=verb_conj(verb_name)
            v=vv[i]
            for j in v.keys():
                # print(v[j])
                verbadd=Verb(verbname=verb_name, tense_id = i, tense = 'NULL', pronoun =j, converb = v[j]) 
                db_session.add(verbadd)
        count = count + 1
    db_session.commit()    

