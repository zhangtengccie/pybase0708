from ssh_router import ssh_cli
from ping import ping_ret
import re
import pprint


def get_interface(*ips, username='cisco', password='cisco'):
    device_if_dict = {}
    for ip in ips:
        ping_ip = ping_ret(ip)
        if ping_ip is True:
            ret = ssh_cli(ip, 'cisco', 'cisco', cmd='show ip int brief')
            interface = re.findall('[A-Z]\S+\d', ret)
            ip_address = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', ret)
            # print(interface)
            # print(ip_address)
            dict_all = {}
            for k,v in zip(interface,ip_address):
                dict_all[k]=v
            device_if_dict[ip]=dict_all


        else:
            device_if_dict[ip] = {}
    return device_if_dict


pprint.pprint(get_interface('1.1.1.200','1.1.1.100','1.1.1.16', username='cisco', password='cisco'),indent=4)