from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from datalayer.connection_string import dbpath
from datalayer.models.feeds.PublishedFeed import PublishedFeed



def is_feed_new(feed_id, source):
    # create engine
    engine = create_engine(f"sqlite:///{dbpath}")

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    existed_feed = session.query(PublishedFeed).filter_by(feed_id=feed_id).first()
    is_it_new = False
    if not existed_feed:
        new_feed = PublishedFeed(feed_id=feed_id, publish_date=datetime.now(), feed_source=source)
        session.add(new_feed)
        session.commit()
        is_it_new = True
    session.close()
    return is_it_new
