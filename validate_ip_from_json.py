import ipaddress
import json


def validate_ip(i):
    try:
        ip = ipaddress.ip_address(i['lanIp'])
        print('%s is a correct IP%s address for device with serial: %s' % (ip, ip.version, i['serial']))
    except ValueError:
        print('%s is an invalid IP address for device with serial: %s' % (i['lanIp'], i['serial']))


data = json.load(open('JSONdata'))

for i in data:
    validate_ip(i)
