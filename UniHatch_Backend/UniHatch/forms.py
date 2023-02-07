from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField 
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date, datetime as dt 
from UniHatch.models import User

class RegistrationForm(FlaskForm):
    firstName = StringField('First Name',
                           validators=[DataRequired(), Length(min=1, max=50)])
    lastName = StringField('Last Name',
                           validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    phoneNumber = StringField('Phone Number', 
                                validators = [DataRequired(), Length(min=10, max =10)])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = IntegerField('zipcode', validators=[DataRequired()])
    Birthday = DateField("Birthday", default=date.today(), format='%d/%m/%Y', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email): 

        user = User.query.filter_by(email = email.data).first()
        if user: 
            raise ValidationError('That email is takem. Please choose another')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class Listing(FlaskForm):
    name = 
    address = StringField('Address', validators = [DataRequired()])
    rentalPrice = StringField('Rent', validators = [DataRequired()])

class searchForm(FlaskForm): 
    location = StringField('Location', validators = [DataRequired()])
    movein = DateField('Move-In Date', default=date.today(), format='%d/%m/%Y', validators=[DataRequired()])
    moveout = DateField('Move-Out Date', default=date.today(), format='%d/%m/%Y', validators=[DataRequired()])
    groupSize = IntegerField('Group Size', validators = [DataRequired()])
    search = SubmitField('Find your Hatch!')

    def validate_moveout(self, moveout, movein):
        if res = (dt.strptime(moveout, '%d/%m/%Y') - dt.strptime(movein, '%d/%m/%Y')).days <= 0:
            raise ValidationError('Please enter a moveout date after your movein')



