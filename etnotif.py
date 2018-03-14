"""Etnotif script"""
import os
import time
import logging

from etnawrapper import EtnaWrapper
import notify2


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


def get_notification():
    notify2.init('etnotif')
    notifier = notify2.Notification('ETNA', message='initialized etnotify')
    notifier.show()
    return notifier


logger = get_logger()

def get_client():
    login = os.environ.get('ETNA_USER')
    password = os.environ.get('ETNA_PASS')
    etna = EtnaWrapper(login=login, password=password)
    infos = etna.get_infos()
    logger.info('logged as {} at {}'.format(infos['login'], infos['login_date']))
    return etna


def get_latest_notification(etna):
    notifications = etna.get_notifications()
    return notifications[0]


def monitor_notifications(client, notifier):
    notif = get_latest_notification(client)
    logger.info('{} : {}'.format(notif['start'], notif['message']))
    for notification in new_notifications(notif, client):
        logger.info(notification)
        notifier.update('ETNA - New notification', message=notification['message'])
        notifier.show()


def new_notifications(old_notif, client):
    while True:
        current_notif = get_latest_notification(client)
        if old_notif != current_notif:
            old_notif = current_notif
            yield current_notif
        else:
            logger.debug('[OLD] %s : %s', current_notif['start'], current_notif['message'])
            time.sleep(5)


def main():
    client = get_client()
    notifier = get_notification()
    notify = get_notification()
    monitor_notifications(client, notify)


if __name__ == "__main__":
    main()
