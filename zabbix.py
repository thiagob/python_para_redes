
from pyzabbix.api import ZabbixAPI

# Create ZabbixAPI class instance
zapi = ZabbixAPI(url='http://192.168.1.161/', user='Admin', password='zabbix')


# List all hosts
hosts = zapi.host.get(monitored_hosts=2, output='extend')

for host in hosts:
    print("Host: %s (ID=%s)" % (host['name'], host['hostid']))


# Create a new host
# https://www.zabbix.com/documentation/2.4/manual/api/reference/host/create
result2 = zapi.do_request('host.create',
    {
        "host": "Linux server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.3.1",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "5"
            }
        ]
    }
)

