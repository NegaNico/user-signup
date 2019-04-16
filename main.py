from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_signup.html')

@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    
    if len(username) < 3 or len(username) > 20:
        username_error = "invalid username (3-20 characters long)"
    if len(password) < 3 or len(password) > 20:
        password_error = "invalid password (3-20 characters long)"
    
    if username == '':
        username_error = "invalid username"
    if password == '':
        password_error = "invalid password"
    if verify_password == '':
        verify_password_error = "Passwords don't match"
    if password != verify_password:
        verify_password_error = "Passwords don't match"        

    if email:
        if len(email) < 3 or len(email) > 20:
            email_error = "invalid email (3-20 characters long)"
        if ' ' in email or '@' not in email or '.' not in email:
            email_error = "invalid email"
    
    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('user_signup.html', username=username, username_error=username_error,
        password_error=password_error, verify_password_error=verify_password_error, 
        email=email, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html", username=username)

app.run()