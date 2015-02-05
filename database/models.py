from sqlalchemy import Column, String, Integer, DateTime
from database.connection import Base

class AllData(Base):
    __tablename__ = 'alldata'

    id = Column(Integer, primary_key=True)
    title = Column(String(1000))
    url = Column(String(1000))
    date = Column(DateTime)

    def __init__(self, id=None, title=None, url=None, date=None):
        self.id = id
        self.title = title
        self.url = url
        self.date = date

    def __repr__(self):
        return "<AllData: id='%d', title='%s', url='%s', date='%s'>" % (self.id, self.title, self.url, self.date)
