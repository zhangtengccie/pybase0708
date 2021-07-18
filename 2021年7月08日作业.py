from ssh_router import  ssh_cli
from ping import ping_ret
import re
import pprint


def qytang_get_if(*ips,username,password):
    device_if_dict= {}
    for ip in ips:
        if_dict ={}
        if ping_ret(ip):
            for line in ssh_cli(ip,username='cisco',password='cisco',cmd='show ip inter brief').split('\n'):
                re_result = re.match(r'([A-Z]\S+\d+)\s+'
                                     r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                                     r'\w+\s+\w+\s+\w+\s+\w+',line.strip())
                if re_result:
                    if_dict[re_result.groups()[0]] = re_result.groups()[1]
        device_if_dict[ip] = if_dict
    return device_if_dict

if __name__ == '__main__':
    pprint.pprint(qytang_get_if('1.1.1.200','1.1.1.33',username='cisco',password='cisco'))