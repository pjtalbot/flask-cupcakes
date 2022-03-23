from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email

class AddCupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    
    
    flavor = StringField("Flavor")
    size = StringField("Size")
    Image = StringField("Picture URL")
    rating = FloatField("Age")
    

class EditCupcakeForm(FlaskForm):

    
    flavor = StringField("Flavor")
    size = StringField("Size")
    Image = StringField("Picture URL")
    rating = FloatField("Age")