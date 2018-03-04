import tornado.ioloop
import tornado.web
from WelcomeUser import sayHello
import json
import os

root = os.path.dirname(__file__)


class APIHandler(tornado.web.RequestHandler):
  def get(self):
    #get the Argument that User had passed as name in the get request
    userInput=self.get_argument('name')
    welcomeString=sayHello(userInput)
    #return this as JSON
    self.write(json.dumps(welcomeString))

def make_app():
  return tornado.web.Application([
      (r"/API/data", APIHandler),
       (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"})
  ])

if __name__ == "__main__":
    app = make_app()
    port = int(os.environ.get("PORT", 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()