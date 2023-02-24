import ipinfo
import pyfiglet
import subprocess
import os
import re
from collections import namedtuple
import configparser

#################################################

heading = pyfiglet.figlet_format("LOC MATTER")
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',heading,'\n\n')

#################################################

while True:
    try:
        ip = input("<< ENTER IP ADDRESS >> ")
    except IndexError:
        ip = None
        
    access_token = 'f1f8b555995306'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip)

    for key, value in details.all.items():
        print(f"{key}: {value}")