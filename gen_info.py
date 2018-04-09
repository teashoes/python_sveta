from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import noun_artikel

engine = create_engine('sqlite:///mybase.db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
class Noun(Base):
    __tablename__ = 'nouns'
    id = Column(Integer, primary_key=True)
    noun_name = Column(String(50))
    artikel = Column(String(50))

    def __repr__(self):
        return '<Noun {} {}>'.format(self.noun_name, self.artikel)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

# from db import db_session, Noun

# me = Noun(noun_name='huis', artikel='het')
noun = input()
me= Noun(noun_name=get_noun(), artikel=get_art(())

db_session.add(me)
db_session.commit()
print(me.noun_name)