#!/usr/bin/env python3
from __future__ import print_function, unicode_literals

print("\n\n\n")

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1 = mac1.strip()
mac2 = mac2.strip()
mac3 = mac3.strip()

ipaddr1 = mac1.split()[1]
ipaddr2 = mac2.split()[1]
ipaddr3 = mac3.split()[1]

macaddr1 = mac1.split()[3]
macaddr2 = mac2.split()[3]
macaddr3 = mac3.split()[3]

print("{:>20}{:>20}".format("IP ADDR", "MAC ADDRESS"))
print("-" * 40)
print("{:>20}{:>20}".format(ipaddr1, macaddr1))
print("{:>20}{:>20}".format(ipaddr2, macaddr2))
print("{:>20}{:>20}".format(ipaddr3, macaddr3))

print("\n\n\n")
