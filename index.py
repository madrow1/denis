
from flask import Flask, render_template, request

# jinja tags

#safe - can be used to pass HTML as a variable in jinja.
#capitalize- capitalises the first letter of every tag.
#lower - makes every word lowercase.
#upper - makes every word uppercase
#title - capitalises the first letter in every word 
#trim
#striptags - strips any HTML tags from a vari

# variables can be called from the html document with {{ $VARIABLE }}
# logic statements can be called from the html document with {% $LOGIC %}

# to pass an input via the URL bar use /<$VARIABLE>/ for example to pass the variable "name" via the URL use "/<name>"

index = Flask(__name__)

@index.route("/")

def index_page():
    return render_template("index.html")

# Create custom error pages 

@index.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404

@index.errorhandler(500)
def server_not_responding():
    return render_template("500.html"), 500


index.run(debug=True)