from database import db_session, Verb
from sqlalchemy import and_, or_, not_
from add_verb_db import verb_add
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

# print(conj_show('verhuizen', 0))