#!/usr/bin/env python3

import os

print(f"Real UID: {os.getuid()}")
print(f"Effective UID: {os.geteuid()}")

