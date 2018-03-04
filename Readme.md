This is a sample Application which shows how you can make calls to a service, which calls a Python function.

This works on [Tornado Web Server](http://www.tornadoweb.org/en/stable/)

To install Tornado, run the following command (via pip)

    pip install tornado
To run this code, run:

    python web_wrapper.py

The code has a `index.html` which makes an Ajax call to the API, sending the name that the user has entered. The service (contained in `web_wrapper.py`) calls a Python file (`WelcomeUser.py`), and sends the name to the function called `sayHello()`