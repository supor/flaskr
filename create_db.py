# -*-coding:utf-8 -*-
from sqlalchemy import Column, String, create_engine, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = 'entries'
    id = Column(String(6), primary_key=True)
    title = Column(String(20))
    text = Column(String(20))


engine = create_engine('mysql://root:@localhost:3306/blog')
DBSession = sessionmaker(bind=engine)
article = Table('entries', DBSession, autoload=True)

session = DBSession()
new_user = Article(id='4', title='hello', text="hello python+flask")
session.add(new_user)
session.commit()
session.close()





