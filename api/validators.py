import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def validateEmail(email):
    if re.search(regex, email):
        return True
    else:
        return False


def validateMessage(req):
    # Check for keys
    if "email" not in req:
        return False, {"message": "Email is required"}, 400

    if "name" not in req:
        return False, {"message": "Name is required"}, 400

    if "message" not in req:
        return False, {"message": "Message is required"}, 400

    email = req["email"]
    name = req["name"]
    message = req["message"]

    # Validate
    if len(email) == 0 or not validateEmail(email):
        return False, {"message": "Invalid Email"}, 400

    if len(name) == 0:
        return False, {"message": "Invalid Name"}, 400

    if len(message) == 0:
        return False, {"message": "Invalid Message"}, 400

    return True, {}, 200
