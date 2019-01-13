from flask import render_template, url_for,flash,redirect
from myproject import app
from myproject.forms import RegistrationForm, LoginForm
from myproject.models import User, Post

posts=[
    {
        'author':'Mariusz Przybysz',
        'title':'Blog Post 1',
        'content':'My first blog post',
        'date_posted':'January 9, 2019'
    },
    
    {
        'author':'Mariusz Przybysz',
        'title':'Blog Post 2',
        'content':'My second blog post',
        'date_posted':'January 10, 2019'
    }]    



@app.route("/")
@app.route("/home")
def home():
    num=8
    return render_template("home_page.html",value=num,title='Home')
    
@app.route("/chat")
def chat():
    return render_template("chat_page.html",title='Chat')

@app.route("/blog")
def blog():
    return render_template("blog_page.html",posts=posts,title='Blog')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form=RegistrationForm() 
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template("register.html",title='Register',form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template("login.html",title='Login',form=form)