from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dhirajbarve143@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'kqfe olup tvnd ufbx'    # Replace with your password
app.config['MAIL_DEFAULT_SENDER'] = 'ankitgodbole90@gmail.com'


mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    date = request.form['date']
    reason = request.form['reason']
    entry_time = request.form['entryTime']
    exit_time = request.form['exitTime']

    # Email content
    subject = f"New Gate Pass Request from {name}"
    body = f"""
    Visitor Name: {name}
    Date of Visit: {date}
    Reason: {reason}
    Entry Time: {entry_time}
    Exit Time: {exit_time or 'Not provided'}
    """

    # Sending email to HOD
    msg = Message(subject, recipients=['malviyashivam238@gmail.com'])  # HOD's email
    msg.body = body
    mail.send(msg)

    flash('Gate pass submitted and email sent to HOD!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'dhiraj_barve123456'
    app.run(debug=True)
