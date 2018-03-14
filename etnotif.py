"""Etnotif script"""
import os

from etnawrapper import EtnaWrapper


def get_client():
    login = os.environ.get('ETNA_USER')
    password = os.environ.get('ETNA_PASS')
    etna = EtnaWrapper(login=login, password=password)
    print(etna.get_infos())
    return etna


def get_latest_notification(etna):
    notifications = etna.get_notifications()
    return notifications[0]

def main():
    client = get_client()
    notif = get_latest_notification(client)
    print(notif)


if __name__ == "__main__":
    main()
