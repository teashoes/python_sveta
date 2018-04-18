from database import db_session, Noun
from noun_artikel import get_art
# noun='moeder'
def noun_add(noun_name):   
    nounadd=Noun(noun=noun_name, artikel=get_art(noun_name))
    
    db_session.add(nounadd)
    db_session.commit()
#     print(nounadd.noun_name)
