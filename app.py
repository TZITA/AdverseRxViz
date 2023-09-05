from flask import Flask, render_template, request, redirect, url_for, flash
from fetch import create_adverse_events_chart
from waitress import serve
from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key = 'TOMZITA'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'thomas.beyene.v2@gmail.com'
app.config['MAIL_PASSWORD'] = 'Tomzita123$'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('viz.html')

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        recipient = 'thomas.beyene.v2@gmail.com'
        mail_subject = f"New Contact Form Submission: {subject}"
        mail_message = f"Name: {name}\n"
        mail_message += f"Email: {email}\n"
        mail_message += f"Subject: {subject}\n"
        mail_message += f"Message:\n{message}"

        msg = Message(mail_subject, sender='thomas.beyene.v2@gmail.com', recipients=[recipient])
        msg.body = mail_message

        try:
            mail.send(msg)
            flash("Message sent successfully.", "success")
            return redirect(url_for('viz.html'))
        except Exception as e:
            flash("An error occurred while sending the message. Please try again later.", "error")
            return redirect(url_for('viz'))

@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    # Get selected checkboxes from the request
    chart_types = request.json

    # Generate the chart based on selected types
    chart_html = create_adverse_events_chart(chart_types)
    return chart_html


if __name__ == '__main__':
    #serve(app)
    app.run(debug=True)