from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

# Form for logging in existing users
class LoginForm(FlaskForm):
    email = StringField(
        "Enter Email",  # Label shown on the form
        validators=[DataRequired(), Email()],  # Must not be empty and must be a valid email
        render_kw={"placeholder": "you@email.com"}  # Text inside input box
    )
    password = PasswordField(
        "Enter Password",  # Label for password field
        validators=[DataRequired()],  # Must not be empty
        render_kw={"placeholder": "Your password"}  # Optional placeholder
    )
    submit = SubmitField("Login")  # Button text

# Form for registering new users
class RegisterForm(FlaskForm):
    name = StringField(
        "Enter Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "John Doe"}
    )
    email = StringField(
        "Enter Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "you@example.com"}
    )
    password = PasswordField(
        "Enter Password",  # Reminder that you’ll validate strength later
        validators=[DataRequired()],
        render_kw={"placeholder": "At least 8 characters, 1 number, etc."}
    )
    submit = SubmitField("Create Account")


