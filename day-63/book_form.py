from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import NumberRange


class BookForm(FlaskForm):
    name = StringField('Name')
    author = StringField('Author')
    rating = DecimalField('Rating', validators=[NumberRange(min=0, max=10)])
    submit = SubmitField('Add Book')
