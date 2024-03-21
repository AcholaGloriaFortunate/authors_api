# from authors_app.extensions import db
#from app.extentions import db,bcrypt
from datetime import datetime
from authors_app.extension import db, migrate




class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)#all datatypes start with capital letter eg Integer,String
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(100),nullable=False)
    image=db.Column(db.String(255),nullable=True)
    email=db.Column(db.String(100),nullable=False,unique=True)
    contact=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.Text(),nullable=False)
    biography=db.Column(db.Text(),nullable=True)
    book=db.relationship('Book',backref='users')
    user_type=db.Column(db.String(20),default='author')
    created_at=db.Column(db.DateTime,default=datetime.now())
    updated_at=db.Column(db.DateTime,onupdate=datetime.now())

    def __init__(self,first_name,last_name,email,contact,password,biography,user_type,image=None):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.user_type=user_type
        self.contact=contact
        self.image=image
        self.biography=biography
        self.password=password







# from flask import Flask
# from authors_app.extension import db
# from datetime import datetime
# from authors_app.extension import db, migrate

# #creating class user
# class User(db.Model):
#     __tablename__ = "users"
#     #creating an instance
#     #unllable means the field is either required or not
#     #primary key and unique are constraits
    
#     id = db.Column(db.Integer, primary_key = True)
#     first_name = db.Column(db.String(50), nullable = False)
#     last_name = db.Column(db.String(100), nullable = False)
#     image = db.Column(db.String(255), nullable = True)
#     email = db.Column(db.String(100), nullable = False, unique = True)
#     contact = db.Column(db.String(50), nullable = False, unique = True)
#     password = db.Column(db.Text(), nullable = False, unique = True)
#     biography = db.Column(db.Text, nullable = True)
#     books = db.relationship('Book', backref= 'user')
#     user_type = db.Column(db.String(20), default='author') #Amin, Author etc
#     created_at = db.Column(db.DateTime, default=datetime.now())
#     updated_at = db.Column(db.DateTime,onupdate=datetime.now())
#     #company = db.relationship('Company', book_populates ='User')
    
    

#     def __init__(self,first_name,last_name,email,contact,password,user_type,image,biography):
#         super(User,self).__init__()
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.contact = contact
#         self.image = image
#         self.biography = biography
#         self.password = password
#         self.user_type = user_type

#     def get_full_name(self):
#         return f'{self.last_name} {self.first_name}'

#     #def set-password(self, password):
    #    self._password = bcrypt.generate_password_hash(password).decode('utf-8')

    

    