from flask import Flask 

app = Flask(__name__) #creating the Flask object as an "app"

@app.route('/') #put your domain here, its a route to where your app will live
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True) #debug mode shows us breakdown of what is wrong, don't have to keep restarting servers

#websites are basically sets of routes 
# website backends are like a set of plugs: when the user clicks a certain button, the user makes a request for certain information
# that information could be a page of campaign jobs, search results, HTML/CSS etc. 
# website frontends are the user interface that the user sees and interacts with 
