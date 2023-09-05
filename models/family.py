from models.base_model import BaseModel, Base
from models.task import Task
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey




class Family(BaseModel, Base):
    __tablename__ = 'families'
    __table_args__ = {"mysql_default_charset": "latin1"}

    name = Column(String(128), nullable=False)
    owner_id = Column(String(60, collation='utf8mb4_unicode_ci'), ForeignKey('users.id'), nullable=False)
    
    # Define a one-to-many relationship to the Task model
    # tasks = relationship('Task', back_populates='family')
    # Create a one-to-many relationship to the User model to represent family members
    # members = relationship('User', back_populates='family')
    tasks = relationship('Task', back_populates='family', foreign_keys=[Task.family_id])
    members = relationship('User', back_populates='family', foreign_keys=[User.family_id])

