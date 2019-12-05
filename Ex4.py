#!/usr/bin/env python3
from __future__ import print_function, unicode_literals

print("\n\n\n")
print("-" * 60)

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()

model = show_version.split()[1]
serial_num = show_version.split()[2]

print(show_version)
print("\n")
print("Model:", model)
print("Serial Number: ", serial_num)
print("\n")
print('Model contains "Cisco"? ', 'cisco' in model.lower())
print('Model contains "881"? ', '881' in model)
print("\n")
print("-" * 60)

print("\n\n\n")
