from functools import wraps

from flask import request


def filterRequests(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            pass
        except Exception as e:
            return {"message": "Server Error"}, 500
        return func(*args, **kwargs)

    return decorated
