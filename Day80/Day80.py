# Day 80 Code

# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/process", methods=["POST"])
# def process():
#   page = ""
#   form = request.form

#   if form["baldies"] == "david":
#     page += f"You're alright {form['username']}"
#   else:
#     page += f"You've picked wrong {form['username']}"
#   return page

# @app.route('/')
# def index():
#   page = """<html><body><form method = "post" action="/process">
#     <p>Name: <input type="text" name="username" required> </p>
#     <p>Email: <input type="Email" name="email"> </p>
#     <p>Website: <input type="url" name="website"> </p>
#     <p>Age: <input type="number" name="age"> </p>
#     <input type="hidden" name="userID" value="232"> </p>

#     <p>
#       Fave Baldy: 
#       <select name="baldies">
#         <option>David</option>
#         <option>Jean Luc Picard</option>
#         <option>Yul Brynner</option>
#       </select>
#     </p>

#     <button type="submit">Save Data</button>
#   </form>
#   </body></html>
#     """
#   return page
  
# app.run(host='0.0.0.0', port=81)

# Day 80 Challenge

from flask import Flask, request

users = {}
users["divya"] = {"email":"divdev@gmail.com","password":"a123"}
users["ria"] = {"email":"riadev@gmail.com","password":"b456"}
users["divyangini"] = {"email":"divpython@gmail.com","password":"div"}

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    form = request.form
    for user in users:
        if user == form["username"] and \
           users.get(form["username"], {}).get("email") == form["email"] and \
           users.get(form["username"], {}).get("password") == form["password"]:
            return open("template/right.html", "r").read()
    return open("template/wrong.html", "r").read()
  
@app.route("/")
def home():
  page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>form</title>
</head>

<body>
 <form method="post" action="/login">
   <p>Username: <input type="text" name="username" required></p>
   <p>Email: <input type="email" name="email" required></p>
   <p>Password: <input type="password" name="password" required></p>
   <button type="submit">Login</button>
 </form>

</body>

</html>"""
  
  return page
  
app.run(host='0.0.0.0', port=81)
