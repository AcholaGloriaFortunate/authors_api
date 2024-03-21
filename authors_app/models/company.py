from authors_app.extension import db
from datetime import datetime


class Company(db.Model):
    
    __tablename__="companies"
    id=db.Column(db.Integer,primary_key=True)#all datatypes start with capital letter eg Integer,String
    name=db.Column(db.String(50),nullable=False)
    origin=db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #user=db.relationship("users",backref="companies")
    created_at=db.Column(db.DateTime,default=datetime.now())
    updated_at=db.Column(db.DateTime,onupdate=datetime.now())

def __init__(self,name,description,origin):
    self.name=name
    self.description=description
    self.origin=origin


    def __init__(self):
        return f"<company(name='{self.name}',origin='{self.origin}')"









# from authors_app import db
# from authors_app.extension import db
# from datetime import datetime

# class Company(db.Model):
#     __tablename__ = 'companies'

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(255), nullable=False, unique=True)
#     origin = db.Column(db.String(100))
#     description = db.Column(db.String(1000))
#     user_id = db.Column(db.Integer, db.foreign_key('users.id'))
#     user = db.relationship('User', backref='companies')
#     created_at = db.Column(db.DateTime, default=datetime.now())
#     updated_at = db.Column(db.DateTime, onupdate=datetime.now())


#     def __init__ (self,name,origin,description,user_id):
#         super(Company, self).__init__()
#         self.name = name
#         self.origin = origin
#         self.description = description
#         self.user_id = user_id

#     # def __repr__(self):
#     #     return f'<Company(name = '{self.name}', origin = '{self.origin}'>'