"""Etnotif script"""
import os
import time

from etnawrapper import EtnaWrapper


def get_client():
    login = os.environ.get('ETNA_USER')
    password = os.environ.get('ETNA_PASS')
    etna = EtnaWrapper(login=login, password=password)
    infos = etna.get_infos()
    print('logged as {} at {}'.format(infos['login'], infos['login_date']))
    return etna


def get_latest_notification(etna):
    notifications = etna.get_notifications()
    return notifications[0]

def monitor_notifications(client):
    notif = get_latest_notification(client)
    print('{} : {}'.format(notif['start'], notif['message']))
    for notification in new_notifications(notif, client):
        print(notification)


def new_notifications(old_notif, client):
    while True:
        current_notif = get_latest_notification(client)
        if old_notif != current_notif:
            old_notif = current_notif
            yield notif
        else:
            print("Same notif")
            time.sleep(5)


def main():
    client = get_client()
    monitor_notifications(client)



if __name__ == "__main__":
    main()
