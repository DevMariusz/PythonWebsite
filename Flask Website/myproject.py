from flask import Flask, render_template

app = Flask(__name__)

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
def hello():
    num=8
    return render_template("home_page.html",value=num,title='Home')
    
@app.route("/chat")
def chatpage():
    return render_template("chat_page.html",title='Chat')

@app.route("/blog")
def blogpage():
    return render_template("blog_page.html",posts=posts,title='Blog')


if __name__ == '__main__':
    app.run(debug=True)