from database import db_session, Verb
from sqlalchemy import and_, or_, not_
# i=input()
# verb=input()
def conj_show(verb, tense):
    reply=[]
    for row in Verb.query.filter(and_(Verb.verbname.like(verb), Verb.tense_id==tense)):
        reply.append(row.pronoun+' '+row.converb)
    return reply


# def find_verb_form(bot, update):
#     user_text = update.message.text 
#     update.message.reply_text(user_text)
#     reply=[]
#     for row in Verb.query.filter(and_(Verb.verbname.like(user_text), Verb.tense_id==0)):
#         reply.append(row.pronoun+' '+row.converb)
#     update.message.reply_text(reply)