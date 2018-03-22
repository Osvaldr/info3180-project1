"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import time

from app import app,db
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
from forms import CreateProfileForm
from models import UserProfile
rootdir = os.getcwd()

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile',methods=['GET', 'POST'])
def addprofile():
    userform = CreateProfileForm()
    if request.method == 'POST':
        if userform.validate_on_submit():
            firstname  = userform.firstname.data
            lastname   = userform.lastname.data
            email      = userform.email.data
            biography  = userform.biography.data
            location   = userform.location.data
            sex        = userform.gender.data
            
            created_on = format_date_joined()
            
            photo      = userform.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename)) 
            
            newUser=UserProfile(first_name=firstname,last_name=lastname,email=email,location=location,sex=sex,created_on=created_on,filename=filename,biography=biography)
            db.session.add(newUser)
            db.session.commit()
            
            flash("User Created")
            return redirect(url_for("viewprofiles"))
        else:
            flash_errors(userform)

            
    return render_template('profile.html',form=userform)
    
  

@app.route('/profiles')
def viewprofiles():
    profiles = db.session.query(UserProfile).all()
    return render_template('profiles.html',profiles=profiles )
    
    
@app.route('/profile/<userid>')
def userprofile(userid):
    User = UserProfile.query.get(userid)
    return render_template("userprofile.html", User=User)
        
def format_date_joined():
    """calculates current date and time"""
    return (time.strftime("%B,%Y"))    
    
    

###
# The functions below should be applicable to all Flask apps.
###
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (getattr(form, field).label.text,error))

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")