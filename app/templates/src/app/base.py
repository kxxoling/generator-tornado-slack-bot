import os
from slackclient import SlackClient

from .config import SLACK_TOKEN


slack_client = SlackClient(SLACK_TOKEN)
