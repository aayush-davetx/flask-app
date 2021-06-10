from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__) #creating the Flask object as an "app"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model): #model for each blogpost instance
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False) 
    author = db.Column(db.String(20), nullable=False, default="N/A")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1. LALALALAL.',
        'author': 'Aayush'
    },
    {
        'title': 'Post 2',
        'content': 'This is post 2. LOOOLOOO'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else: 
        return render_template('edit.html', post=post)

#put your domain here, its a route to where your app will live
@app.route('/home/users/<string:name>/posts/<int:id>') #can have different ids for images, accounts, posts
def hello(id, name):
    return "Hello, " + name + " your id is: " + str(id)

@app.route('/onlyget', methods=['GET']) #only allow this webpage to do GET requests
def get_req():
    return 'You can only get this webpage. 5'

if __name__ == "__main__":
    app.run(debug=True) #debug mode shows us breakdown of what is wrong, don't have to keep restarting servers

#websites are basically sets of routes 
# website backends are like a set of plugs: when the user clicks a certain button, the user makes a request for certain information
# that information could be a page of campaign jobs, search results, HTML/CSS etc. 
# website frontends are the user interface that the user sees and interacts with 
