from flask import Flask, render_template, request
from flask_mail import Mail, Message

from config import MAIL_PASSWORD, MAIL_USERNAME

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    msg = Message('New Portfolio Contact',
                  sender=email,
                  recipients=['prakruthisomashekar29@gmail.com'])
    msg = Message('New Message from Portfolio', sender=email, recipients=['prakruthisomashekar29@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    
    mail.send(msg)

if __name__ == '__main__':
    app.run()
