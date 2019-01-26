from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField, SubmitField, validators


class TokensForm(Form):

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
