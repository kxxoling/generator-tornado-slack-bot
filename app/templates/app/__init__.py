import logging
from tornado.web import RequestHandler
from tornado.web import Application
from .config import *  # noqa


class SlackBotHandler(RequestHandler):
    def post(self):
        args = self.request.arguments
        if SLACK_WEBHOOK_TOKEN not in args.get('token'):
            raise Exception('Token not match!')
        channel_name = args.get('channel_name')
        username = args.get('user_name')
        text = args.get('text')
        echo_msg = '{username} in {channel_name} said: "{text}"'.format(
            username=username,
            channel_name=channel_name,
            text = text,
        )
        logging.debug(echo_msg)
        self.finish()

    def get(self):
        self.finish('hello')


def make_app():
    return Application([
        (r'/slack', SlackBotHandler),
    ])
