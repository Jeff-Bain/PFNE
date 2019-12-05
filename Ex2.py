#!/usr/bin/env python3
from __future__ import print_function

print("\n\n\n")

try:
    ip_addr = raw_input("Please enter an IP address: ")
except NameError:
    ip_addr = input("Please enter an IP address: ")

octets = ip_addr.split(".")
octet1 = int(octets[0])
octet2 = int(octets[1])
octet3 = int(octets[2])
octet4 = int(octets[3])

print("\n\n")
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(octet1, octet2, octet3, octet4))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(octet1), bin(octet2), bin(octet3), bin(octet4)))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(octet1), hex(octet2), hex(octet3), hex(octet4)))
print("-" * 60)

print("\n\n\n")
