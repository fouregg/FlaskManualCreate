from main import another_app
from flask import request
from flask import make_response

''' test web hook
@another_app.before_request
def test():
    print("Hi")
'''

class User:
    def __init__(self, id_user, name):
        self.id_user = id_user
        self.name = name


def load_user(user_id):
    if user_id == "42":
        return User(42, "Alexey")
    elif user_id == "100":
        return User(100, "Dima")
    else:
        return None

def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello, you browser is {}</h1>'.format(user_agent)

'''
@another_app.route("/user/<name>") # В скобках меньше больше мыф пишем параметр, передаваемый в url
def hello_user(name):
    return '<h2>Hello, {}<h2>'.format(name)
'''

@another_app.route("/bad_request")
def bad_fill(code=400):
    print("test")
    return '<h3>Bad Request<h3>', code


@another_app.route("/custom_response")
def cust_response():
    response = make_response("<H1>Put this in cookie!<H1>")
    response.set_cookie('answer', '42')
    return response


@another_app.route("/user/<user_id>")
def get_user(user_id):
    user = load_user(user_id)
    if user is None:
        return bad_fill(404)
    else:
        return '<h1>Hello, {}<h1>'.format(user.name)


another_app.add_url_rule("/", "index", index) # Эквивалент декоратора 'name_app'.route('url')