from flask import Flask
from flask_mail import Mail

app = Flask(__name__, template_folder='Templates')
app.config['SECRET_KEY'] = 'd21ef2b582d668cf0f791ad33b8e386cc9f81e7e'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'sj706640@gmail.com'
app.config['MAIL_PASSWORD'] = 'ewgmytimibxludyq'
mail = Mail(app)

from Application import routes
