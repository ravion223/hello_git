from sqlalchemy import ForeignKey, Integer, String, Column
from .engine import Base

class DBUser(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)