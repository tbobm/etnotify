
Etnotify
========

ETNA Notification watcher.
Gets informations about the latest validations.

Install
-------

..

   This project won't work inside a virtualenv because of the dbus dependency.


.. code-block:: bash

   $ git clone https://github.com/tbobm/etnotify
   $ cd etnotify
   $ pip install -r requirements.txt
   $ python etnotify.py

Configuration
-------------

.. code-block:: bash

   $ export ETNA_USER=yourlogin
   $ export ETNA_PASS=yourpassword

Aim of the Etnotify
-------------------

Ever felt like something important on the intranet was missing ? Like notifications?

This script aims to fix that, by allowing you to be alarmed when something new happens.

In a rush ?
~~~~~~~~~~~

You'll get notified if your validation requests have been accepted or rejected, in the blink of an eye.
