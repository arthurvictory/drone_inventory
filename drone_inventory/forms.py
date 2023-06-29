from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('E-mail', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()


class DroneForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    price = DecimalField('price', places = 2)
    camera_quality = StringField('camera quality')
    flight_time = StringField('flight time')
    max_speed = StringField('max speed')
    dimensions = StringField('dimensions')
    weight = StringField('weight')
    cost_of_production = DecimalField('cost of production', places = 2)
    series = StringField('series')
    dad_joke = StringField('dad joke')
    submit_button = SubmitField() 