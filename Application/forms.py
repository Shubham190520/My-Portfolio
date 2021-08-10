from flask_wtf import FlaskForm
from wtforms import SubmitField


class submit(FlaskForm):
    submit = SubmitField(label='Send Message')
