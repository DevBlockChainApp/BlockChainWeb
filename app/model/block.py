from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.base_class import Base


class Block(Base):
    __tablename__ = 't_block'
    __table_args__ = ({'schema': 'bchain', 'comment': 'Users'})

    id = Column(Integer, primary_key=True, index=True)
    body = Column(String, index=True)
    hash = Column(String, index=True)
    # date_create = Column(DateTime, server_default=datetime.now())
