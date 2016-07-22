from tornado.ioloop import IOLoop

from app import make_app


application = make_app()
application.listen(8000)
IOLoop.current().start()
