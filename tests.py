import os

import etnotify


def test_get_client():
    client = etnotify.get_client()
    assert client is not None
