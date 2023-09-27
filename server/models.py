from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
# from datetime import datetime
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
# db = SQLAlchemy()
class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialize_rules=('-baked_goods.bakery',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime,server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())
    baked_goods = db.relationship('BakedGood',backref='bakery')


    def __repr__(self):
        return f'bakeries(id={self.id}), ' + \
            f'name={self.name}, ' + \
            f'created_at={self.created_at}, ' + \
            f'updated_at={self.updated_at}' 

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialize_rules=('-bakery.baked_goods',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime,onupdate=db.func.now())

    # bakery = db.relationship('Bakery',backref='baked_goods')
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

    def __repr__(self):
        return f'BakedGood(id={self.id}), ' + \
            f'name={self.name}, ' + \
            f'price={self.price}, ' + \
            f'bakery_id={self.bakery_id}, ' + \
            f'created_at={self.created_at}, ' + \
            f'updated_at={self.updated_at}'
            
