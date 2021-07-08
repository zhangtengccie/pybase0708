import logging
from kamene.all import *
from kamene.layers.inet import ICMP, IP

logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *
def ping_ret(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return True
    else:
        return False
    

if __name__ == '__main__':

    print(ping_ret('1.1.1.1'))