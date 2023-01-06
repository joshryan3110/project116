# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Mike Bobaguard" # write your name
    age = "8" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/Father")
def home():

    name = "Douglas Bobaguard" 
    age = "59" 

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/Mother")
def home():

    name = "Patricia Bobaguard"
    age = "37"

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/Friend")
def home():

    name = "George Dickinson" 
    age = "8"

    return render_template('friend.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
