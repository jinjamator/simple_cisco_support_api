import getpass
from simple_cisco_support_api import CiscoSupportAPIClient
from pprint import pprint

cisco_support=CiscoSupportAPIClient()
cisco_support.login(input("client_id:"),getpass.getpass("client_secret:"))
pprint(cisco_support.api.bug('v3.0').bugs.bug_ids.CSCwc66053.get())

