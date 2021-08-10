from Application import app, mail
from flask import render_template, request
from flask_mail import Message
from Application.forms import submit


@app.route('/', methods=['GET', 'POST'])
def home():
    form = submit()

    if form.validate_on_submit():
        mail_message = f'Name: {request.form.get("name_client")}\n' \
                       f'Email: {request.form.get("email")}\n' \
                       f'Subject: {request.form.get("subject")}\n' \
                       f'Message: {request.form.get("message-box")}\n'
        messages = Message(subject='A message from Portfolio Website', sender='sj706640@gmail.com',
                           recipients=['sj706640@gmail.com'])
        messages.body = mail_message
        mail.send(messages)
    return render_template('index.html', form=form)
