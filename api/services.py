import logging

import requests
from flask_mail import Message

from api import app, mail
from flask import render_template


def sendMeMail(req):
    with app.app_context():
        email = req["email"]
        name = req["name"]
        message = req["message"]

        mailMessage = Message(
            subject="Contacting from Portfolio",
            sender=app.config['MAIL_USERNAME'],
            recipients=[
                app.config['MY_EMAIL'],
            ]
        )

        mailMessage.body = """Hey Paargav. You have a message.\n\nName - {}\nEmail - {}\nMessage - {}\n""".format(name,
                                                                                                                  email,
                                                                                                                  message)

        mailMessage.html = render_template(
            "sendMeTemplate.html",
            name=name,
            email=email,
            message=message
        )

        mail.send(mailMessage)
        logging.info("PORTFOLIO : Sent mail to me")


def sendConfirmationMail(req):
    with app.app_context():
        email = req["email"]
        name = req["name"]

        mailMessage = Message(
            subject="Thanks for contacting",
            sender=app.config['MAIL_USERNAME'],
            recipients=[
                email
            ]
        )

        mailMessage.body = """Hey {}. Your message has reached me successfully. I'll contact you back as soon as 
        possible. Cheers 😄.""".format(name)

        mailMessage.html = render_template(
            "sendConfirmationTemplate.html",
            name=name
        )

        mail.send(mailMessage)
        logging.info("PORTFOLIO : Sent mail to visitor - {}".format(name))


def sendMails(req):
    # sendMeMail(req)
    # sendConfirmationMail(req)

    return {
               "message": "Mail sent successfully."
           }, 200


def verifyReCaptcha(recaptcha, remote_addr):
    verifyUrl = """https://www.google.com/recaptcha/api/siteverify?secret={}&response={}&remoteip={}""".format(
        app.config['RECAPTCHA_PRIVATE_KEY'], recaptcha, remote_addr)

    resp = requests.post(verifyUrl)
    response = resp.json()

    if not response['success']:
        return False, {"message": "reCaptcha verification failed"}, 400

    return True, {}, 200
