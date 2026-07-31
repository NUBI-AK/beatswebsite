from flask import render_template, request, redirect, url_for, flash
from forms import LoginForm, RegisterForm
from models import Beat

def init_app(app):

    @app.route("/")
    def home():
        beats = Beat.query.all()
        # Pass current_page so navbar knows we're on home
        return render_template("homepage.html", beats=beats, current_page="home")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            # Example: just print the data for now
            email = form.email.data
            password = form.password.data
            flash("Login attempted!", "info")
            return redirect(url_for("home"))

        # Pass current_page so navbar hides Login link
        return render_template("login.html", form=form, current_page="login")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            flash("Account created!", "success")
            return redirect(url_for("login"))

        # Pass current_page so navbar hides Register link
        return render_template("register.html", form=form, current_page="register")