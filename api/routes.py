import logging

from flask import request

from api import app
from api.services import sendMails, verifyReCaptcha
from api.validators import validateMessage


@app.route("/", methods=["GET"])
def home():
    return {"message": "Hello from API"}, 200


@app.route("/send-mail", methods=["POST"])
def send_mail():
    try:
        req = request.get_json(force=True)

        # Validate
        condition, msg, status = validateMessage(req)

        # Validation check
        if not condition:
            return msg, status

        # reCaptcha Verification
        condition, msg, status = verifyReCaptcha(req['recaptcha'], request.remote_addr)

        if not condition:
            return msg, status

        # Send Mail
        return sendMails(req)

    except Exception as e:
        logging.error("PORTFOLIO : Error sending mail - {}".format(e))
        return {"message": "Server Error. Please try after sometime."}, 500
