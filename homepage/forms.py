from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    sectors = StringField('업종', validators=[DataRequired(), Length(min=1, max=25)])
    salery = IntegerField('연봉', validators=[DataRequired()])
    region = StringField('지역', validators=[DataRequired(), Length(min=3, max=25)])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])