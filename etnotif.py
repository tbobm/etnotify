"""Etnotif script"""
import os

from etnawrapper import EtnaWrapper


def get_client():
    login = os.environ.get('ETNA_USER')
    password = os.environ.get('ETNA_PASS')
    print(login)
    print(password is not None)
    etna = EtnaWrapper(login=login, password=password)
    print(etna.get_infos())
    return etna


def main():
    get_client()


if __name__ == "__main__":
    main()
