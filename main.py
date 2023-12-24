# Import flask 
from flask import Flask 
from flask_cors import CORS    

# Initialize flask app 
app = Flask(__name__)
CORS(app)

# Endpoint 1    
@app.route('/')
def home():
    return "Hello, World!"

# Endpoint 2  
@app.route('/aboutme')
def myInfo():
    return {"Role": "I am a Software Engineer!"} 

# Endpoint 3
@app.route("/organization")
def myOrganization():
    return {"Name": "Asante Inc", "Industry" : "Engineering"}

# Endpoint 4 
@app.route('/chart')
def get_chart():
    groups = ['group A', 'group B', 'group C']    
    sets = {"set_1":[4, 3, 5], "set_2":[1, 6, 3], "set_3": [2, 5, 6]}

    myData = {"myGroups":groups, "mySets": sets}
    return myData


# Driver 
if __name__ == "__main__":
    app.run(debug=True)       