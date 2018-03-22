from . import db

class UserProfile(db.Model):
    
    id          = db.Column(db.Integer, primary_key=True)
    first_name  = db.Column(db.String())
    last_name   = db.Column(db.String())
    biography   = db.Column(db.String())
    email       = db.Column(db.String())
    location    = db.Column(db.String())
    sex         = db.Column(db.String())
    created_on  = db.Column(db.String())
    filename    = db.Column(db.String())


    def __repr__(self):
        return '<User %r>' % (self.username)
