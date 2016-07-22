from .base import slack_client


def list_channels():
    channels_rsp = slack_client.api_call('channels.list')
    if channels_rsp.get('ok') is True:
        return channels_rsp['channels']
    return None


def get_channel_info(channel_id):
    channel_info = slack_client.api_call('channels.info', channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None


def send_message(channel_id, message):
    slack_client.api_call(
        'chat.postMessage',
        channel=channel_id,
        text=message,
        username='bot',
        icon_emoji=':robot_face:'
    )
