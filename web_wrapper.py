import tornado.ioloop
import tornado.web
from WelcomeUser import sayHello
import json


class APIHandler(tornado.web.RequestHandler):
  def get(self):
    #get the Argument that User had passed as name in the get request
    userInput=self.get_argument('name')
    welcomeString=sayHello(userInput)
    #return this as JSON
    self.write(json.dumps(welcomeString))

def make_app():
    return tornado.web.Application([
        (r"/API/data", APIHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8111)
    tornado.ioloop.IOLoop.current().start()