Introduction
==================

simple_cisco_support_api is a simplified REST Client for the Cisco Support API


Features
-----------------

simple_cisco_support_api has following features:
    * manage login
    * CRUD interface for all possible API URLs

Installation
------------

Install simple_cisco_support_api by running:

.. code-block:: bash

    pip3 install simple_cisco_support_api


Examples
---------

Get Infos For A Specific Bug
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import getpass
    from simple_cisco_support_api import CiscoSupportAPIClient
    from pprint import pprint

    cisco_support=CiscoSupportAPIClient()
    cisco_support.login(input("client_id:"),getpass.getpass("client_secret:"))
    pprint(cisco_support.api.bug('v3.0').bugs.bug_ids.CSCwc66053.get())



Contribute
----------

- Issue Tracker: https://github.com/jinjamator/simple_cisco_support_api/issues
- Source Code: https://github.com/jinjamator/simple_cisco_support_api

Roadmap
-----------------

Selected Roadmap items:
    * add more documentation
    * add some more examples

For documentation please refer to https://simple_cisco_support_api.readthedocs.io/en/latest/

License
-----------------

This project is licensed under the Apache License Version 2.0