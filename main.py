from scapy.all import *
import logging as log
import os
from scapy.all import IP, DNSRR, DNSQR, UDP, DNS
from netfilterqueue import Netfilterqueue

os.system("sudo iptables -I FORWARD -j NFQUEUE --queue-num 1")
queue = Netfilterqueue()
queue.bind(queueNum, callback)
queue.run()

