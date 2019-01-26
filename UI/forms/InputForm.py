from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField, SubmitField, validators
from flask_wtf.file import FileField, FileAllowed, FileRequired


class InputForm(Form):
    code_text = TextAreaField('Write Down Your Code Here', [validators.DataRequired('Code Input is Empty')])
    upload_file = FileField('Upload Your File', validators=[
        FileRequired('You must upload a file'),
        FileAllowed(['c', 'txt'], 'only .c and .txt file can been uploaded')
    ])
    submit_btn = SubmitField('Show Tokens and Generate Output')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
