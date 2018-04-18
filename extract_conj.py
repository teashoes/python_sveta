from database import db_session, Verb
from sqlalchemy import and_, or_, not_
from add_verb_db import verb_add
from add_noun_db import noun_add
from sqlalchemy import func

def conj_show(verb, tense):
    reply=[]
    # rows = session.query(func.count(Congress.id)).scalar()
    if Verb.query.filter(and_(Verb.verbname.like(verb), Verb.tense_id==tense)).count() != 0:
        for row in Verb.query.filter(and_(Verb.verbname.like(verb), Verb.tense_id==tense)):
            reply.append(row.pronoun+' '+row.converb)
    else:
        verb_add(verb)
        for row in Verb.query.filter(and_(Verb.verbname.like(verb), Verb.tense_id==tense)):
            reply.append(row.pronoun+' '+row.converb)
    return reply

def noun_show(noun):
    reply=[]
    if Noun.query.filter(Noun.noun_name.like(noun)).count() != 0:
        for row in Noun.query.filter(Noun.noun_name.like(noun)):
            reply.append(row.artikel+' '+row.noun_name)
    else:
        noun_add(noun)
        for row in Noun.query.filter(Noun.noun_name.like(noun)):
            reply.append(row.artikel+' '+row.noun_name)        
    return(reply)

# print(conj_show('verhuizen', 0))
