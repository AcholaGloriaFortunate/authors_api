from authors_app.extension import db
from datetime import datetime
from authors_app.models.user import User
from sqlalchemy import Column, Integer, String


class Book(db.Model):
    __tablename__='books'
    id=db.Column(db.Integer,primary_key=True)#all datatypes start with capital letter eg Integer,String
    title=db.Column(db.String(50),nullable=False)
    price=db.Column(db.String(100),nullable=False)
    pages=db.Column(db.Integer)
    description=db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # company_id=db.Column(db.Integer,db.ForeignKey('companies.id'))
    publication_date=db.Column(db.Date,nullable=False)
    isbn = db.Column(db.String(30), nullable=True, unique=True)
    genre = db.Column(db.String(50), nullable=False)

    user=db.relationship('user',backref='books')
    #company=db.relationship('company',backref='books')
    created_at=db.Column(db.DateTime,default=datetime.now())
    updated_at=db.Column(db.DateTime,onupdate=datetime.now())


    def __init__(self,title,description,pages,image,price,price_unit,publication_date,isbn,genre,user_id,):
        self.title=title
        self.description=description
        self.price = price
        self.price_unit = price_unit
        self.pages = pages
        self.publication_date = publication_date
        self.isbn = isbn
        self.genre = genre
        self.user_id = user_id
        self.image = image

        self.user_id=user_id
        self.pages=pages



    def __init__(self):
        return f'<Book{self.title}'

















# from authors_app.extension import db
# from datetime import datetime

# class Book(db.Model):
#     __tablename__ = 'books'
#     id = db.Column(db.Interger, primary_key = True)
#     title = db.Column(db.String(100), nullable = False)
#     pages = db.Column(db.Integer,nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#     price_unit = db.Column(db.String(50), nullable=False, default='UGX')
#     publication_date = db.Column(db.Date, nullable=False)
#     isbn = db.Column(db.String(30),nullable=True, unique=True)
#     genre =  db.Column(db.String(50),nullable=False)
#     description = db.column(db.String(255),nullable=False)
#     image = db.Column(db.String(255), nullable=True)
#     user_id = db.Column(db.Integer, db.foreign_key('users.id'))
#     company_id = db.Column(db.Integer, db.foreign_key('companies.id'))
#     #users = db.relationship('User', backref='books')
#     #Company = db.relationship ('Companies', backref = 'books')
#     created_at = db.Column(db.DateTime, default=datetime.now())
#     updated_at = db.Column(db.dateTime, onupdate=datetime.now())
#     #price = db.Column(db.Float)
#     user = db.relationship('User', backref='books')
#     company = db.relationship('Company', backref='books')
#     #user_id = db.Column(db.Integer,db.foreign_key('users.id'))

#     def __init__(self, title, description, pages, user_id):
#         self.title = title
#         self.description = description

#         self.user_id = user_id
#         self.pages = pages

#     def __repr__(self):
#         return f'<Book {self.title}>'

    