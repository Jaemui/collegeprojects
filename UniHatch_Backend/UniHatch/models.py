from datetime import datetime, date
from UniHatch import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(120), unique = True, nullable = False)
    lastName = db.Column(db.String(120), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False )
    password = db.Column(db.String(60), nullable = False)
    phoneNumber = db.Column(db.String(10), unique = True, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    zipcode = db.Column(db.Integer(5), nullable = False)
    Birthday = db.Column(db.Date(), nullable = False)
    lisitng = db.relationship('Listing', backref = 'Property Manager', lazy= True)

    def __repr__ (self): 
        return f"User('{self.firstName}', '{self.lastName}','{self.email}', '{self.password}', '{self.phoneNumber}','{self.city}', '{self.state}', '{self.state}', '{self.zipcode}', '{self.Birthday}')" 

class Listing(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable =False )
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(20), nullable =False )
    state = db.Column(db.String(20), nullable =False )
    zipcode = db.Column(db.Integer(5), nullable =False )
    # photos = db.Column(db.String())
    listingDescription = db.Column(db.String(1000), nullable = False)
    rating = db.Column(db.Integer())
    rent = db.Column(db.Integer())
    category = db.Column(db.String(100))
    availableStart = db.Column(db.date())
    availableEnd = db.Column(db.date())
    bathroomCount = db.Column(db.Integer())
    bedroomCount = db.Column(db.Integer())
    applicationFee = db.Column(db.Integer())
    securityDeposit = db.Column(db.Integer())
    groupSize = db.Column(db.Integer())
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50), nullable = False)
    movein = db.Column(db.Date(), nulable = False)
    moveout= db.Column(db.Date(), nullable = False)
    groupSize = db.Column(db.Integer())






