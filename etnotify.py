#!/usr/bin/env python
"""Etnotif script"""
import os
import time
import logging

from etnawrapper import EtnaWrapper
from etnawrapper import BadStatusException

import requests

try:
    import notify2

    PLATFORM = "LINUX"
except ImportError:
    from win10toast import ToastNotifier

    PLATFORM = "WINDOWS"


def get_logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if os.environ.get('DEBUG'):
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    return logger


def send_notification(notifier, title, message):
    if PLATFORM == "LINUX":
        notifier.update(
            title,
            message
        )
        notifier.show()
    else:
        notifier.show_toast(
            title,
            message,
            icon_path="etna.ico",
            duration=10
        )


def get_notification():
    if PLATFORM == "LINUX":
        notify2.init('etnotif')
        notifier = notify2.Notification('ETNA', message='initialized etnotify')
    else:
        notifier = ToastNotifier()
    send_notification(notifier, "ETNA", 'initialized etnotify')
    return notifier


logger = get_logger()


def get_client():
    login = os.environ.get('ETNA_USER')
    password = os.environ.get('ETNA_PASS')
    etna = EtnaWrapper(login=login, password=password)
    infos = etna.get_infos()
    logger.info(
        'logged as {} at {}'.format(infos['login'], infos['login_date'])
    )
    return etna


def get_latest_notification(etna):
    try:
        notifications = etna.get_notifications()
    except BadStatusException as err:
        logger.exception('Something bad happened.')
        return str(err)
    except requests.exceptions.SSLError:
        logger.info('SSL error')
        return 'SSL Error'
    except Exception as err:
        logger.exception('err, something unplanned happened. bad bad bad.')
        return str(err)
    return notifications[0]


def monitor_notifications(client, notifier):
    notif = get_latest_notification(client)
    logger.info('{} : {}'.format(notif['start'], notif['message']))
    for notification in new_notifications(notif, client):
        logger.info(notification)
        try:
            send_notification(notifier, 'ETNA - New notification', notification['message'])
        except Exception as err:
            send_notification(notifier, 'ETNOTIFY - Error', str(err))


def new_notifications(old_notif, client):
    while True:
        current_notif = get_latest_notification(client)
        if current_notif is False:
            logger.error('Could not get a notification. Calling for help.')
            yield {'message': 'ERROR while getting notification.'}
        elif old_notif != current_notif:
            old_notif = current_notif
            yield current_notif
        else:
            logger.debug(
                '[OLD] %s : %s',
                current_notif['start'],
                current_notif['message']
            )
            time.sleep(5)


def main():
    client = get_client()
    notify = get_notification()
    monitor_notifications(client, notify)


if __name__ == "__main__":
    main()
