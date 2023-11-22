# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Yatharth" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def first_webpage():    
    name = 'Flask'
    return render_template('father.html', index_variable = name)

# define the route to mother webpage
@app.route("/mother")
def second_webpage():    
    name = 'Flask'
    return render_template('mother.html', index_variable = name)

# define the route to friends webpage
@app.route("/friends")
def third_webpage():    
    name = 'Flask'
    return render_template('friend.html', index_variable = name)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
