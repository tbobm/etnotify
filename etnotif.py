"""Etnotif script"""
import os
import time

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
    while True:
        new_notif = get_latest_notification(client)
        if notif != new_notif:
            print(new_notif)
            notif = new_notif
        else:
            print("Same notif")
            time.sleep(5)



if __name__ == "__main__":
    main()
