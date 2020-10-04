from datetime import datetime
from app import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return einfo.query.get(user_id)

class einfo(db.Model, UserMixin):

    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    E_Name=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(20),nullable=False)
    admin=db.Column(db.Boolean,nullable=False)
    visibility=db.Column(db.Boolean,nullable=False)

class P_Info(db.Model):
    P_id=db.Column(db.String(20),unique=True,primary_key=True)
    P_Name=db.Column(db.String(20),nullable=False)
    visibility=db.Column(db.Boolean,nullable=False)

class TimeShift(db.Model):
    T_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    id=db.Column(db.Integer)
    P_id=db.Column(db.String(20))
    Date=db.Column(db.String(20))
    Head=db.Column(db.String(20))
    House=db.Column(db.String(20))
    Time=db.Column(db.String(20))
    Description=db.Column(db.String(20))
    Field=db.Column(db.String(20))
    Verified=db.Column(db.Boolean)
