#!/usr/bin/python3
""" create a web application that listens on port 5000
"""


from flask import Flask
app = Flask(__name__)
# condition strict_slashes=False
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ print this message
    """
    return ("Hello HBNB!")


@app.route('/hbnb')
def no_hello():
    """ print another message
    """
    return ("HBNB")


if __name__ == "__main__":
    # config the run
    app.run(host='0.0.0.0', port=5000)
