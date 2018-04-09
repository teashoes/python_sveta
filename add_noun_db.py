from database import db_session, Noun
from noun_artikel import get_art
noun='moeder'

nounadd=Noun(noun_name=noun, artikel=get_art(noun))

db_session.add(nounadd)
db_session.commit()
print(nounadd.noun_name)
