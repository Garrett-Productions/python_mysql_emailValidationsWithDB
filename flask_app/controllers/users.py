from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User 

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)


@app.route("/create_user", methods = ['POST'])
def create_user():
    if not User.validate_user(request.form):
        #if there are errors then redirect back to our form
        return redirect ('/')
        #no errors, capture info into a dictionary and save the data and redirect elsewhere
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    newID = User.save(data)
    print(newID)
    # Don't forget to redirect after saving to the database.
    return redirect(f"/read_one/{newID}")


@app.route("/read_one/<int:id>")
def read_one(id):
    data = {
        "id": id
    }
    user = User.get_one_user(data)
    print(user)
    return render_template("user.html", one_user = user)


@app.route("/read_all")
def read_all():
    users = User.get_all()
    return render_template("index2.html", users=users)


@app.route("/update_one/<int:id>")
def update_one(id):
    data = {
        "id": id
    }
    user = User.get_one_user(data)
    return render_template("edit_user.html", one_user = user)


@app.route("/make_changes/<int:id>", methods=["POST"])
def make_changes(id):
    data = { 
        "id": id,
        "email": request.form['email'],
        "f_name": request.form['f_name'],
        "l_name": request.form['l_name']
        }
    user = User.update_user(data)
    return redirect(f"/read_one/{ id }")


@app.route("/delete_user/<int:id>")
def delete_user(id):
    data = {
        "id": id
        }
    User.delete_user(data)
    return redirect('/')

