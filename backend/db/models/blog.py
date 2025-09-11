from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from db.base_class import Base

class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='blogs')
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)