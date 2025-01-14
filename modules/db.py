from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine("sqlite:///spam.db", echo=True)
base = declarative_base()


class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)


base.metadata.create_all(engine)


class db:
    session = sessionmaker(bind=engine)()

    def insert_user(self, user_id, username, first_name, last_name, auto_commit=True):
        self.session.add(
            User(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
            )
        )
        if auto_commit:
            self.session.commit()

    def commit(self):
        self.session.commit()

    def clear_users(self):
        pass
        # здесь нужно реализовать очистку всех данных в таблице пользователей
        # self.session.

    def get_users(self):
        pass
        # здесь нужно реализовать получение всех объектов из бд. я не помню через что можно в telethon получить сущность пользователя. вроде бы можно и через id
        # self.session.query(User).sele
