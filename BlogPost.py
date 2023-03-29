from flask import *
from flask.templating import render_template
from databasemodule import *

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/register_author")
def regauthor():
    return render_template("Author form.html")

@app.route("/register_user")
def reguser():
    return render_template("User form.html")

@app.route("/Authorform",methods=["POST"])
def authorform():
    usr=request.form["username"]
    pwd=request.form["password"]
    emailid=request.form["email"]
    cityname=request.form["city"]
    t=(usr,pwd,emailid,cityname)
    add_author_data(t)
    return redirect("/")

@app.route("/Userform",methods=["POST"])
def userform():
    usr=request.form["uname"]
    pwd=request.form["pwd"]
    email=request.form["emailid"]
    city=request.form["cityname"]
    t=(usr,pwd,email,city)
    add_user_data(t)
    return redirect("/")

@app.route("/loginform",methods=["POST"])
def loginform():
    usr=request.form["selectuser"]
    loginid=request.form['loginid']
    password=request.form['password']
    t=(loginid,password)
    if 'author'==usr:
        uname=check_author_login(t)
        if uname:
            return render_template("Author interface.html",res=uname[0])
        else:
            return redirect("/")
    elif 'user'==usr:
        uname=check_user_login(t)
        if uname:
            all_blog=all_author_view_post()
            return render_template("all post.html",res=uname[0],res2=all_blog)
        else:
            return redirect("/")

@app.route("/addpost/<data>")
def addnewpost(data):
    return render_template("add new post.html",res=data)

@app.route("/viewpost/<data>")
def viewposts(data):
    author_data=author_view_post(data)
    return render_template("view posts.html",res=data,res2=author_data)

@app.route("/Addnewpost/<data>",methods=["POST"])
def adding_post(data):
    author_name=request.form["authorname"]
    blog_title=request.form["blogtitle"]
    blog=request.form["blog"]
    t=(author_name,blog_title,blog)
    add_new_post(t)
    return render_template("add new post.html",res=data)

@app.route("/logout")
def logout():
    return redirect("/")

@app.route("/imghome/<data>")
def imghome(data):
    return render_template("Author interface.html",res=data)

if(__name__=="__main__"):
    app.run(debug=True)
