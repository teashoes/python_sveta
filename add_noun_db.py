from database import db_session, Noun
from noun_artikel import get_art
# noun='moeder'
def noun_add(noun_n):   
    nounadd=Noun(noun_name=noun_n, artikel=get_art(noun_n))
    
    db_session.add(nounadd)
    db_session.commit()
#     print(nounadd.noun_name)
