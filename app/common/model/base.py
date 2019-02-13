from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Integer, Column
from contextlib import contextmanager
from flask import current_app


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            if not current_app.config['IGNORE_SQL_FALSE']:
                raise e
            yield


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    id = Column('id', Integer, primary_key=True)
