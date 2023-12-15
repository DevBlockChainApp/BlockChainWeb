from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, DateTime, Integer, String, text

from app.db.base_class import Base


class Block(Base):
    __tablename__ = 't_block'
    __table_args__ = ({'schema': 'bchain', 'comment': 'Main chain table'})

    index = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)
    date_create = Column(TIMESTAMP, server_default=text('now()'))
    hash_block = Column(String, index=True)
    prev_hash = Column(String, index=True)
