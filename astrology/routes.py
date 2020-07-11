from flask import render_template, url_for, redirect, request, flash
from astrology import app, crypt, Users, Dh, Ast

logged_in = False
logged_in_detail = None

@app.route('/')
def home():
    return render_template('home.html', ast=Ast, logged_in=logged_in)

@app.route('/freehoroscope/<string:sign>')
def signhoroscope(sign):
    x = Dh.find_one({'_id':sign})
    imgpath = None
    
    if x:
            # If Zodiac Sign Present in the Database
        imgpath = '../static/images/' + x['_id'].lower() + '.png'
    else:
        print('No such Zodiac Sign Found!')
    return render_template('freehoroscope.html', signdata=x, imgpath=imgpath, logged_in=logged_in)

@app.route('/talk-to-astrologer')
def tta():
    return render_template('talktoastrologer.html', astrcrsr = Ast, logged_in=logged_in)

@app.route('/annual-horoscope')
def annualhoroscope():
    return render_template('annualhoroscope.html', logged_in=logged_in)

def check_data(email):
    ''' Function to check the existence of a user detail containing the given email, and return the user details if present '''
    
    query = {"email": email}
    x = Users.find_one(query)
    return x

@app.route('/login', methods=['GET','POST'])
def login():
    message = None
    alert = 'danger'
    global logged_in
    global logged_in_detail
    
    if request.method == "POST":
            # Extracting Data from Login form
        login_email = request.form.get('login_email')
        login_password = request.form.get('login_password')
        detail = check_data(login_email)    # Checking for the existence of the email in the database
        logged_in_detail = detail
        
        if detail:
                # Checking if the User Detail present for the enterd Email
            if crypt.check_password_hash(detail["password"], login_password):
                    # Checking Encrypted password with the entered one
                logged_in = True
                return redirect('/')
            else:
                message = 'Invalid Email or Password!'
                logged_in = False
        else:
            message = 'Invalid Email or Password!'
            logged_in = False
    return render_template('login.html', title='Login', logged_in=logged_in, user=logged_in_detail, message=message, alert=alert)

@app.route('/logout')
def logout():
    global logged_in
    logged_in=False
    return redirect('/')    # Redirecting to Homepage

def save_data(fname, lname, mobile, email, password):
    ''' Function to Save the given user details in the Database '''
    
    value = {"first_name":fname, "last_name":lname, "mobile":mobile, "email":email, "password":password}
    x = Users.insert_one(value)    # Inserting the given User Details in the database

def is_present(key,value):
    ''' Function to check the key value pair in the Database '''
    
    query = {key:value}     # Setting criteria for searhing a given key value pair
    x = Users.find_one(query)       # Checking for the presence of the key value pair
    if x:
        return True
    else:
        return False

@app.route('/register', methods=['GET','POST'])
def register():
    message=None
    global logged_in
    alert = "danger"
    
    if request.method == 'POST':
            # Extracting Data from the Register form
        reg_fname = request.form.get('firstname')
        reg_lname = request.form.get('lastname')
        reg_mobile = request.form.get('mobile')
        reg_email = request.form.get('register_email')
        reg_password = request.form.get('register_password')
        reg_confirm = request.form.get('register_confirm')

        if is_present("email",reg_email):
                # If enterd Email already present in the Database
            message="Email Already Registered. Enter Another One!"
        elif reg_password != reg_confirm:
                # If Passwords do not Match
            message="Password Do Not Match!"
        else:
            hashed_password = crypt.generate_password_hash(reg_password).decode('utf-8')    # Encrypting Password
            save_data(reg_fname, reg_lname, reg_mobile, reg_email, hashed_password)
                # Saving the new user details, including encrypted password, in the database
            
            message = 'You Have Been Registered. You May Login!'
            alert = "success"
    return render_template('register.html', title='Register', logged_in=logged_in, message=message, alert=alert)