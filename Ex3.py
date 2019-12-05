#!/usr/bin/env python3
from __future__ import print_function, unicode_literals

print("\n\n\n")
print("-" * 60)

ip_six_address = "2620:127:7001:100::53"
IP_SIX_ADDRESS = "2620:127:7001:611::22"
ipv6_address = "2620:127:7001:FFFF::99"

print(ip_six_address)
print(IP_SIX_ADDRESS)
print(ipv6_address)
print("\n")
print("Address1 == Address2? ", ip_six_address == IP_SIX_ADDRESS)
print("Address1 != Address3? ", ip_six_address != ipv6_address)
print("\n")
print("-" * 60)

print("\n\n\n")
