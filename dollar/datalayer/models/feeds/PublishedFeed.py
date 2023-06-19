from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PublishedFeed(Base):
    __tablename__ = 'published_feeds'

    feed_id = Column(String, primary_key=True)
    publish_date = Column(DateTime)
    feed_source = Column(String)
