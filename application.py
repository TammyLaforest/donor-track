from flask import Flask, flash, redirect, render_template, request, session, url_for, g, Markup, make_response
from flask_sqlalchemy import SQLAlchemy
import os
from app import db
from models import result
import psycopg2
from sqlalchemy.dialects.postgresql import JSON
# basedir = os.path.abspath(os.path.dirname(__file__))
# https://donor-track.herokuapp.com/
# https://git.heroku.com/donor-track.git

# configure application
app = Flask(__name__)
app.config['SQLAlchemy_TRACK_Modifications'] = False
DATABASE_URL = os.environ['DATABASE_URL']
app.config.from_object(os.environ['APP_SETTINGS'])
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app.config['SQLAlchemy_DATABASE_URI'] = os.environ['DATABASE_URL']
db.SQLAlchemy(app)











@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)


class User(bd.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = 'this-really-needs-to-be-changed'
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# class ProductionConfig(Config):
#     DEBUG = False


# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#
#
# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#
#
# class TestingConfig(Config):
#     TESTING = True





from setuptools import setup, find_packages


from flask_session import Session
from flask_session.__init__ import Session

from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from jinja2 import Environment, PackageLoader, select_autoescape

from helpers import *



# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# from cs50 import SQL
# configure CS50 Library to use SQLite database
# db = SQL("sqlite:///donationtracker.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/deposit")
def deposit():
    return render_template("deposit.html")

@app.route("/workspace")
def workspace():
    return render_template("workspace.html")

#     # select each symbol owned by the user and it's amount
#     portfolio_symbols = db.execute("SELECT shares, symbol \
#                                     FROM portfolio WHERE id = :id", \
#                                     id=session["user_id"])

#     # create a temporary variable to store TOTAL worth ( cash + share)
#     total_cash = 0

#     # update each symbol prices and total
#     for portfolio_symbol in portfolio_symbols:
#         symbol = portfolio_symbol["symbol"]
#         shares = portfolio_symbol["shares"]
#         stock = lookup(symbol)
#         total = shares * stock["price"]
#         total_cash += total
#         db.execute("UPDATE portfolio SET price=:price, \
#                     total=:total WHERE id=:id AND symbol=:symbol", \
#                     price=usd(stock["price"]), \
#                     total=usd(total), id=session["user_id"], symbol=symbol)

#     # update user's cash in portfolio
#     updated_cash = db.execute("SELECT cash FROM users \
#                                WHERE id=:id", id=session["user_id"])

#     # update total cash -> cash + shares worth
#     total_cash += updated_cash[0]["cash"]

#     # print portfolio in index homepage
#     updated_portfolio = db.execute("SELECT * from portfolio \
#                                     WHERE id=:id", id=session["user_id"])


# stocks=updated_portfolio, \
#                             cash=usd(updated_cash[0]["cash"]), total= usd(total_cash) )

# @app.route("/buy", methods=["GET", "POST"])
# @login_required
# def buy():
#     """Buy shares of stock."""

#     if request.method == "GET":
#         return render_template("buy.html")
#     else:
#         # ensure proper symbol
#         stock = lookup(request.form.get("symbol"))
#         if not stock:
#             return apology("Invalid Symbol")

#         # ensure proper number of shares
#         try:
#             shares = int(request.form.get("shares"))
#             if shares < 0:
#                 return apology("Shares must be positive integer")
#         except:
#             return apology("Shares must be positive integer")

#         # select user's cash
#         money = db.execute("SELECT cash FROM users WHERE id = :id", \
#                             id=session["user_id"])

#         # check if enough money to buy
#         if not money or float(money[0]["cash"]) < stock["price"] * shares:
#             return apology("Not enough money")

#         # update history
#         db.execute("INSERT INTO histories (symbol, shares, price, id) \
#                     VALUES(:symbol, :shares, :price, :id)", \
#                     symbol=stock["symbol"], shares=shares, \
#                     price=usd(stock["price"]), id=session["user_id"])

#         # update user cash
#         db.execute("UPDATE users SET cash = cash - :purchase WHERE id = :id", \
#                     id=session["user_id"], \
#                     purchase=stock["price"] * float(shares))

#         # Select user shares of that symbol
#         user_shares = db.execute("SELECT shares FROM portfolio \
#                            WHERE id = :id AND symbol=:symbol", \
#                            id=session["user_id"], symbol=stock["symbol"])

#         # if user doesn't has shares of that symbol, create new stock object
#         if not user_shares:
#             db.execute("INSERT INTO portfolio (name, shares, price, total, symbol, id) \
#                         VALUES(:name, :shares, :price, :total, :symbol, :id)", \
#                         name=stock["name"], shares=shares, price=usd(stock["price"]), \
#                         total=usd(shares * stock["price"]), \
#                         symbol=stock["symbol"], id=session["user_id"])

#         # Else increment the shares count
#         else:
#             shares_total = user_shares[0]["shares"] + shares
#             db.execute("UPDATE portfolio SET shares=:shares \
#                         WHERE id=:id AND symbol=:symbol", \
#                         shares=shares_total, id=session["user_id"], \
#                         symbol=stock["symbol"])

#         # return to index
#         return redirect(url_for("index"))


@app.route('/login', methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    return render_template("login.html")



    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("Must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("Must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users \
                           WHERE username = :username", \
                           username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("workspace"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html")


@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("Please provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("Please provide password")

        # ensure password and verified password is the same
    elif request.form.get("password") != request.form.get("verification"):
            return apology("passwords do not match")

            new_user = User(name)
            db.session.add(new_user)
            # Commit for INSERT and REMOVE Statements
            db.session.commit()

            users = User.query.order_by(User.id).all()

            # insert the new user into users, storing the hash of the user's password
            # result = db.execute("INSERT INTO users (username, hash) \
            #                      VALUES(:username, :hash)", \
            #                      username=request.form.get("username"), \
            #                      hash=pwd_context.encrypt(request.form.get("password")))

            if not result:
                return apology("Username already exist")

                # remember which user has logged in
                session["user_id"] = result

                # redirect user to home page
                return redirect(url_for("index"))

            else:
                return render_template("login.html")
