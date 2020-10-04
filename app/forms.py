from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,IntegerField,RadioField,BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from app.models import einfo

class SignupForm(FlaskForm):
    fullname = StringField('Fullname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_email(self,email):
        email=einfo.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email Already Registered,Reset Password?')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UpdateForm(FlaskForm):
    fullname = StringField('fullname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    update = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            email=einfo.query.filter_by(email=email.data).first()
            if email:
                    raise ValidationError('Email Already Registered,Reset Password?')

    def validate_name(self,fullname):
        if fullname.data != current_user.E_Name:
            E_Name=einfo.query.filter_by(E_Name=fullname.data).first()
            if E_Name:
                    raise ValidationError('Name Already Registered,Reset Password?')
class AdminAssignForm(FlaskForm):

     submit = SubmitField('Assign Task')

class NewProjectForm(FlaskForm):
    P_Name = StringField('P_Name',
                       validators=[DataRequired(), Length(min=2, max=20)])
    P_id = StringField('P_id',
                    validators=[DataRequired()])
    submit = SubmitField('Click Here')

class ReportAssignForm(FlaskForm):
    loopid=IntegerField('loopid')
    date=DateField('startdate',format='%Y-%m-%d',validators=[DataRequired()])
    Head=StringField('Head',validators=[DataRequired()])
    House=RadioField('House',choices=[('Inhouse','Inhouse'),('Outhouse','Outhouse')],validators=[DataRequired()])
    Time=StringField('Time',validators=[DataRequired()])
    Description=StringField('Description',validators=[DataRequired()])

class ReportNonAssignForm(FlaskForm):
    date=DateField('date',format='%Y-%m-%d',validators=[DataRequired()])
    Head=StringField('Head',validators=[DataRequired()])
    House=RadioField('House',choices=[('Inhouse','Inhouse'),('Outhouse','Outhouse')],validators=[DataRequired()])
    Time=StringField('Time',validators=[DataRequired()])
    Description=StringField('Description',validators=[DataRequired()])
    Field=StringField('Field',validators=[DataRequired()])
    submit = SubmitField('Click Here')

class DateForm(FlaskForm):
    date=DateField('date',format='%Y-%m-%d',validators=[DataRequired()])
