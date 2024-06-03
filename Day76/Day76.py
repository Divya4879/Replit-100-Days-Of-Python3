# Day 76- Flask

# from flask import Flask 
# # Imports the flask library
# import datetime

# app = Flask(__name__,static_url_path="/static")
# # Starts the Flask application. The 'app' variable is very important. We'll be using that later.

# @app.route('/')
# # Tells the code what to do if we've gone to our web address with just a / after the URL
# def index():
#   # Tells the code which webpage to show. This subroutine will display the 'Hello from Flask' page
  
#     # return 'Hello from Flask!'
#     page = f"""<html><body><p><a href="/home">HomePage</a></p></body></html>"""

#     return page

# @app.route('/home') # Creates the path to the home page
# def home(): # Subroutine to create the home page
#   # Three quotes followed by the html for the baldies site. Three more quotes to close. All the HTML is assigned to the 'page' variable
#   date = datetime.date.today()
#   page = f"""<html>

#   <head>
#     <title>David's World Of Baldies</title>
#   </head>


#   <body>
#   <h1>Dave's World of Baldies</h1> 
#   <h2>Welcome to our website on {date}.</h2>

#   <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

#   <h2>Gallery of Baldies</h2>
#   <p>Here are some of the legends of the bald world.</p>

#   <img src="static/images/picard.jpg" width = 30%> 
#   <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

#   <ul>
#     <li>Beautiful bald man</li>
#     <li>Calm and cool under pressure</li>
#     <li>All the Picard memes</li>
#   </ul>

#   <p><a href = "page2.html">Go to page 2</a></p>

# </body>

# </html>

#   """

#   return page # returns the contents of the page variable


# app.run(host='0.0.0.0', port=81)
# # This line should ALWAYS come last. It's the line that turns on the Flask server.

# Fix The Code

# from flask import Flask
# import datetime # import the datetime library

# app = Flask(__name__,static_url_path="/static")


# @app.route('/')
# def index(): 
#   page = f"""<html><body>
#   <p><a href = "/home">Go home</a></p>
#   </body>
#   </html>"""
#   return page

# @app.route('/home') 
# def home(): 
#   page = """<html>

#   <head>
#     <title>David's World Of Baldies</title>
#   </head>


#   <body>
#   <h1>Dave's World of Baldies</h1> 
#   <h2>Welcome to our website!</h2>

#   <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

#   <h2>Gallery of Baldies</h2>
#   <p>Here are some of the legends of the bald world.</p>

#   <img src="static/images/picard.jpg" width = 30%> 
#   <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

#   <ul>
#     <li>Beautiful bald man</li>
#     <li>Calm and cool under pressure</li>
#     <li>All the Picard memes</li>
#   </ul>

#   <p><a href = "page2.html">Go to page 2</a></p>

# </body>

# </html>

#   """

#   return page

# app.run(host='0.0.0.0', port=81)


# DAY 76 CHALLENGE

from flask import Flask
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def index():
  page= """<html>
  <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <link href="static/css/index.css" rel="stylesheet" type="text/css" />
  
</head><body>
  <h2>Hello, people!</h2>
  <h3>Do you wanna check out my previous projects below?</h3>
  <p><a href="/Portfolio">1. Portfolio</a></p>
  <p><a href="/LinkTree">2. LinkTree</a></p>
  </body></html>"""
  return page
  
@app.route('/Portfolio')
def portfolio(): 
  page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Portfolio</title>
  <link href="static/css/styles.css" rel="stylesheet" type="text/css" />
  
</head>

<body>
  <h1>Divya - Python Portfolio</h1>

  <img src = "https://i.pinimg.com/originals/35/35/00/3535009c4a5e1d6c611dc436183b2be3.gif">

  <p class="special"><br><br>Hello folks, it's just me sharing my 5 most favourite projects of this journey in Replit Python Challenge so far!</p>

  <div class="title">
  <h2>Project 1 - <u>Python Library Creation</u> 🐍🏛️</h2>
  </div>
  <div>  
  <p>I created a Python Library with my most used functions until that time.</p>
  <a href="https://replit.com/@divyasingh0803/My-Library"><img src="static/images/day 63.jpg" width = "70%"></a>
  <h3>Features:-</h3>
  <ol>
    <li>1: Different color codes' subroutine.</li>
    <li>2: Subroutine for creating,extending, and deleting items of a List.</li>
    <li>3: Subroutine for creating,extending, and deleting items of a Dictionary.</li>
    <li>4: Subroutine for creating,extending, and deleting items of a 2-D List.</li>
  </ol>
  </div>

  <div class="title">
    <h2>Project 2 - <u>Dweeter</u> 🐇🐇<u>,
      Social Media Application</u></h2>
  <div>
  <p>I created a pretty simple version of X, Dweeter, just for myself.</p>
  <a href="https://replit.com/@divyasingh0803/Dwitter-Your-Personal-Twitter"><img src="static/images/day 61.jpg" width = "70%"></a>
  <h3>Features:-</h3>
  <ol>
    <li>1: Add a dweet.</li>
    <li>2: View all my dweets so far.</li>
    <li>3: Delete the dweet I don't want.</li>
  </ol>
  </div>

  <div class="title">
    <h2>Project 3 - <u>Secure Secret Diary</u> 🔏📒</h2>
  </div>
  <div>
  <p>I created an application to serve as my Private Diary.</p>
  <a href="https://replit.com/@divyasingh0803/Secured-Secret-Diary"><img src="static/images/day 72.jpg" width = "70%"></a>
  <h3>Features:-</h3>
  <ol>
    <li>1: Secure Login System (Against peepers & hackers).</li>
    <li>2: Adding new entries.</li>
    <li>3: Viewing all entries, beginning with latest first.</li>
    <li>4: Viewing entries by date.</li>
    <li>5: Deleting an entry.</li>
  </ol>
  </div>

  <div class="title">
    <h2>Project 4 - <u>To-Do List</u> 🗒️</h2>
  </div>
  <div>
  <p>I created a Python Library with my most used functions until that time.</p>
  <a href="https://replit.com/@divyasingh0803/To-Do-List-Management-System-with-backups?v=1"><img src="static/images/day 55.jpg" width = "70%"></a>
  <h3>Features:-</h3>
  <ol>
    <li>1: Adding tasks in our To-Do List, with their deadlines & priorities</li>
    <li>2: Viewing our To-Do List.</li>
    <li>3: Viewing tasks of a specific priority.</li>
    <li>4: Editing items our To-Do.</li>
    <li>5: Removing a task once it's completed.</li>
  </ol>
  </div>

  <div class="title">
    <h2>Project 5 - <u>Epic Character Battle </u>⚔️⚔️</h2>
  </div>
  <div style="margin-bottom: 40px;">
  
  <p>A text-based game about an epic battle between 2 legends of your choice..</p>
  <a href="https://replit.com/@divyasingh0803/BATTLE-OF-LEGENDS"><img src="static/images/Day 28.jpg" width = "70%"></a>
  <h3>Features:-</h3>
  <ol>
    <li>1: User choses 2 characters/plays with another player/computer.</li>
    <li>2: An epic battle ensues between the characters.</li>
    <li>3: Their stats are updated every round.</li>
    <li>4: One character emerges as the winner at the end when another character dies.</li>
  </ol>
  </div>

  <p class="special">That's it! Hope you liked them as well 😊😊🫧💗✨</p>

</body>

</html>
  """

  return page

@app.route('/LinkTree')
def linktree(): 
  page = """<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="static/css/styles2.css" rel="stylesheet" type="text/css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>
  

<img class="profile" src="static/images/download.jpg">

<div class="intro">
<h1>Divya</h1>
<h3>A Python Coder & Web Developer </h2> 
</div>
  
<div class="social">
  <i class="fa fa-linkedin" style="color:white"></i>&nbsp&nbsp
  <a href="https://www.linkedin.com/in/divya-singh-444b4b190/">Linkedin</a>
</div>

  <div class="social">
    <i class="fa fa-twitter-square" style="color:white"></i>&nbsp&nbsp
    <a href="https://twitter.com/Divya67274866">X</a>
  </div>

  <div class="social">
    <i class="fa fa-github" style="color:white"></i>
    &nbsp&nbsp
    <a href="https://github.com/Divya4879">Github</a>
  </div>


  <div class="social">
    🐍👩🏻‍💻&nbsp&nbsp
    <a href="https://f5867c2f-0de6-4756-9af3-073012bca3f1-00-6kebj9ntxfiy.pike.replit.dev/">Python Portfolio</a>
  </div>
  



</body>

</html>
  """

  return page 
app.run(host='0.0.0.0', port=81)
