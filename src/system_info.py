#!/usr/bin/env python3
"""
System information script.
"""

import platform
import os

print("System Information")
print("------------------")
print(f"Operating System: {platform.system()}")
print(f"OS Release: {platform.release()}")
print(f"Python Version: {platform.python_version()}")
print(f"Current Directory: {os.getcwd()}")
print(f"Current User: {os.getlogin()}")
