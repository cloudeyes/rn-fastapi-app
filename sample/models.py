from sqlalchemy import Column, Integer, Boolean, String
from .database import Base


class User(Base):
    __tablename__ = 'app_user'

    email = Column(String(100), primary_key=True, index=True)
    name = Column(String(100), index=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=True)
