from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from noun_artikel import get_art

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

class Verb(Base):
    __tablename__ = 'verb'
    id= Column(Integer, primary_key=True)
    verbname = Column(String(50))
    tense_id = Column(Integer)
    tense = Column(String(50))
    pronoun = Column(String(50))
    converb = Column(String(50))

    def __repr__(self):
        return '<Verb {} {} {} {} {}>'.format(self.verbname, self.tense_id, self.tense, self.pronoun, self.converb)

# class Transl(Base):
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)


