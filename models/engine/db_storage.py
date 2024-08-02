"""
    Contains the class DBStorage
    
    
    Requirements:
            pip install sqlalchemy python-dotenv 
            common class need:
                from sqlalchemy.ext.declarative import declarative_base
                Base = declarative_base()
    """
import os
from dotenv import load_dotenv
from models.common import Base 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



classes = {
    
}


class DBStorage:
    version = '0.1.0'
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        load_dotenv()
        db_user = os.getenv('CARTOFIX_USERNAME')
        db_password = os.getenv('CARTOFIX_PASSWORD')
        db_host = os.getenv('CARTOFIX_HOST')
        db_name = os.getenv('CARTOFIX_DATABASE')
        self.__engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}')
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if self.__session is None:
            raise Exception("Session is not initialized")
        
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        if self.__session is None:
            raise Exception("Session is not initialized")
        
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        if self.__session is None:
            raise Exception("Session is not initialized")
        
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if self.__session is None:
            raise Exception("Session is not initialized")
        
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        if self.__session:
            self.__session.remove()

    def get(self, cls, id):
        """Returns the object based on the class name and its ID, or None if not found"""
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        return all_cls.get(f"{cls.__name__}.{id}", None)

    def count(self, cls=None):
        """count the number of objects in storage"""
        if self.__session is None:
            raise Exception("Session is not initialized")
        
        if not cls:
            count = 0
            for clas in classes.values():
                count += len(self.all(clas))
        else:
            count = len(self.all(cls))
        return count