from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String())


    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"
    

    # tasks = relationship('Task',backref="users")
    # tasks = relationship('Task', back_populates='user')

class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    description = Column(String())
    status = Column(String())
    user_id = Column(Integer(), ForeignKey('users.id'))


    # user = relationship('User', back_populates='tasks')

    # categories = relationship('Category', secondary=task_category_association, back_populates='tasks')

class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    # tasks = relationship('Task', secondary=task_category_association, back_populates='categories')

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"                