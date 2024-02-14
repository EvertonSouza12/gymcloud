from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    
    # Workouts = relationship("Workouts", back_populates="username")
    
# class Workouts(Base):
#     __tablename__ = "workouts"
    
#     id = Column(Integer, primary_key=True)
#     A = Column(String)
#     B = Column(String)
#     C = Column(String)
#     D = Column(String)
#     E = Column(String)
#     username_id = Column(String, ForeignKey("users.username"))
    
#     usernamed = relationship("Users", back_populates="workouts")
    