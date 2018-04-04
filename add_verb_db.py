from database import db_session, Verb
from verbs import verb_conj

verb_name='willen'

for i in range(0,6,1):
    vv=verb_conj(verb_name)
    v=vv[i]
    for j in v.keys():
        # print(v[j])
        verbadd=Verb(verbname=verb_name, tense_id = i, tense = 'NULL', pronoun =j, converb = v[j]) 
        db_session.add(verbadd)
        db_session.commit()
